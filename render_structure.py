import json
import sys
from pathlib import Path


def load_data(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def render_tree(node, indent=0, prefix="", is_last_child=False):
    lines = []
    label = f"{node['id']}  {node['label']}"
    if indent == 0:
        lines.append(label)
    else:
        connector = "└── " if is_last_child else "├── "
        line = "    " * (indent - 1) + connector + label
        lines.append(line)
    children = node.get("children", [])
    for i, child in enumerate(children):
        sub_last = i == len(children) - 1
        lines.extend(render_tree(child, indent + 1, "", sub_last))
    return lines


def fmt_attrs(attrs):
    if not attrs:
        return "-"
    parts = []
    for k, v in attrs.items():
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v)
        elif isinstance(v, bool):
            v = str(v)
        parts.append(f"{k}={v}")
    return " | ".join(parts)


def fmt_preconditions(preconditions):
    if not preconditions:
        return "-"
    parts = []
    for k, v in preconditions.items():
        if k.startswith("_"):
            op, val = v
            parts.append(f"{k[1:]} {op} {val}")
        else:
            parts.append(f"{k}={v}")
    return ", ".join(parts)


def collect_part_ids(node):
    ids = [(node["id"], node.get("label", ""))]
    for child in node.get("children", []):
        ids.extend(collect_part_ids(child))
    return ids


def main():
    data = load_data("structure.json")
    meta = data["meta"]
    tree = data["tree"]
    states = data.get("states", {})

    md = []
    md.append("# 页面结构图")
    md.append("")
    md.append(f"> 更新: {meta['updated']}  |  视口约定: {meta['viewport']}")
    md.append("")

    # ── 零件树 ──
    md.append("## 零件树")
    md.append("")
    md.append("```")
    md.extend(render_tree(tree))
    md.append("```")
    md.append("")

    # ── 状态字典 ──
    md.append("## 状态字典")
    md.append("")

    all_ids = collect_part_ids(tree)
    for pid, plabel in all_ids:
        entries = states.get(pid)
        if not entries:
            continue
        role = entries[0].get("role", "")
        role_text = f"  <i>角色: {role}</i>" if role else ""

        md.append(f"### {pid}  — {plabel}{role_text}")
        md.append("")
        md.append(f"| 状态 | 前置条件 | 特征 | 备注 |")
        md.append(f"|------|----------|------|------|")
        for st in entries:
            name = st["name"]
            cond = fmt_preconditions(st.get("preconditions", {}))
            attr = fmt_attrs(st.get("attrs", {}))
            note = st.get("note", "")
            note_display = "⚠" if note else "-"
            md.append(f"| {name} | {cond} | {attr} | {note_display} |")
        md.append("")
        has_notes = any(st.get("note") for st in entries)
        if has_notes:
            for st in entries:
                note = st.get("note")
                if note:
                    md.append(f"**{st['name']}** 备注:")
                    for line in note.split("\n"):
                        md.append(f"> {line}")
                    md.append("")

    md_text = "\n".join(md)
    out_path = Path("page-structure.md")
    out_path.write_text(md_text, encoding="utf-8")
    print(f"OK → {out_path.resolve()}")


if __name__ == "__main__":
    main()
