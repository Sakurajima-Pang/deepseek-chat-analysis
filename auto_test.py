import json
import random
import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

DATA_DIR = Path(__file__).parent
STRUCTURE_FILE = DATA_DIR / "structure.json"
PERSISTENT_DIR = r"C:\Users\15291\.config\opencode\playwright_data"
URL = "https://chat.deepseek.com/"


def load_structure():
    with open(STRUCTURE_FILE, encoding="utf-8") as f:
        return json.load(f)


async def get_element_state(page, selector):
    return await page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            const rect = el.getBoundingClientRect();
            return {
                classes: Array.from(el.classList),
                width: Math.round(rect.width),
                height: Math.round(rect.height),
                x: Math.round(rect.left),
                childCount: el.children.length
            };
        }""",
        selector
    )


async def get_element_center(page, selector):
    return await page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            const rect = el.getBoundingClientRect();
            return {
                x: rect.left + rect.width / 2,
                y: rect.top + rect.height / 2
            };
        }""",
        selector
    )


async def detect_current_states(page, structure):
    states_def = structure.get("states", {})
    detected = {}

    def find_sel(node, pid):
        if node["id"] == pid:
            return node.get("selector")
        for c in node.get("children", []):
            r = find_sel(c, pid)
            if r:
                return r
        return None

    for pid, entries in states_def.items():
        sel = find_sel(structure["tree"], pid)
        if not sel:
            continue
        cur = await get_element_state(page, sel)
        if not cur:
            continue
        for entry in entries:
            expected = entry.get("attrs", {})
            exp_classes = expected.get("classes", [])
            if exp_classes:
                if len(exp_classes) == len(cur["classes"]) and all(c in cur["classes"] for c in exp_classes):
                    detected[pid] = entry["name"]
                    break
    return detected


async def human_click(page, selector):
    box = await get_element_center(page, selector)
    if not box:
        print(f"  [FAIL] element not found: {selector}")
        return False, box

    offset_x = random.randint(-8, 8)
    offset_y = random.randint(-5, 5)
    target_x = box["x"] + offset_x
    target_y = box["y"] + offset_y

    print(f"  [CLICK] target: ({target_x:.0f}, {target_y:.0f})  offset: ({offset_x:+d}, {offset_y:+d})")

    steps = random.randint(6, 12)
    for i in range(1, steps + 1):
        t = i / steps
        cx = target_x * t + random.randint(-3, 3)
        cy = target_y * t + random.randint(-3, 3)
        await page.mouse.move(cx, cy)
        await asyncio.sleep(random.uniform(0.015, 0.06))

    await asyncio.sleep(random.uniform(0.08, 0.25))
    await page.mouse.click(target_x, target_y)
    return True, box


async def verify_state_change(page, structure, before, expected_after):
    print("\n  [VERIFY] checking state change...")
    await asyncio.sleep(0.5)
    after = await detect_current_states(page, structure)
    all_ok = True
    for pid, expected in expected_after.items():
        actual = after.get(pid, "[not found]")
        before_val = before.get(pid, "-")
        if actual == expected:
            status = "[PASS]"
        else:
            status = "[FAIL]"
            all_ok = False
        print(f"  {status} {pid}: {before_val} -> {actual}  (expect: {expected})")
    return all_ok, after


async def main():
    data = load_structure()
    print("=" * 60)
    print("chat.deepseek.com auto click test")
    print("=" * 60)

    action = sys.argv[1] if len(sys.argv) > 1 else "detect"

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=PERSISTENT_DIR,
            headless=False,
            no_viewport=True,
        )
        page = context.pages[0] if context.pages else await context.new_page()
        if "chat.deepseek.com" not in page.url:
            await page.goto(URL)
            await asyncio.sleep(2)

        print("\n[INFO] detecting page state...")

        # 第一轮：基于 class 精确匹配
        current_states = await detect_current_states(page, data)

        # 第二轮：填充依赖零件（通过 preconditions 推断）
        states_def = data.get("states", {})
        for pid, entries in states_def.items():
            if pid in current_states:
                continue
            for entry in entries:
                preconds = entry.get("preconditions", {})
                if all(current_states.get(k) == v for k, v in preconds.items()):
                    current_states[pid] = entry["name"]
                    break
        sidebar_state = current_states.get("sidebar", "unknown")
        print(f"  sidebar: {sidebar_state}")
        for pid, st in sorted(current_states.items()):
            print(f"  {pid}: {st}")

        if sidebar_state == "unknown":
            print("[WARN] cannot detect sidebar state, exit")
            await context.close()
            return

        if action == "detect":
            print("\n[INFO] detection only, no click performed")
            await context.close()
            return

        if action == "collapse":
            test = {
                "name": "collapse sidebar (click collapse button)",
                "part": "sidebar-inner-header-actions-collapse",
                "selector": "div._7d1f5e2",
                "expected": {"sidebar": "收起", "sidebar-inner": "隐藏", "sidebar-handle": "可见"},
            }
        elif action == "expand":
            test = {
                "name": "expand sidebar (click expand button in handle)",
                "part": "sidebar-handle-actions-expand",
                "selector": "div.e5bf614e > div:nth-child(2)",
                "expected": {"sidebar": "展开", "sidebar-inner": "展开"},
            }
        elif action == "expand-icon":
            test = {
                "name": "expand sidebar (click whale icon)",
                "part": "sidebar-handle-icon",
                "selector": "div._6acebc2",
                "expected": {"sidebar": "展开", "sidebar-inner": "展开"},
            }
        else:
            print(f"[WARN] unknown action: {action}")
            await context.close()
            return

        print(f"\n{'=' * 50}")
        print(f"[ACTION] {test['name']}")
        print(f"  part: {test['part']}")
        print(f"  selector: {test['selector']}")
        print(f"  expected: {test['expected']}")

        before_states = current_states.copy()
        ok, center = await human_click(page, test["selector"])
        if not ok:
            await context.close()
            return

        await asyncio.sleep(0.5)
        ok, new_states = await verify_state_change(page, data, before_states, test["expected"])

        if ok:
            print(f"\n  [PASS] test passed")
        else:
            print(f"\n  [WARN] test did not fully pass")

        await context.close()


if __name__ == "__main__":
    asyncio.run(main())
