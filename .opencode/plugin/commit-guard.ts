import type { Plugin } from "@opencode-ai/plugin"

// Org policy: CI/CD workflow files are not allowed in **sneppx-alg** — it has
// no local C toolchain and no CI, so workflows there cannot be verified.
// Verify with per-file pytest or cmake instead.
//
// This repo (SneppX/.github) IS the correct home for org-default workflows, so
// they are allowed here. sneppx-alg carries its own copy of this guard, so the
// check below only needs to catch commands that explicitly target it.
const SNEPPX_ALG = /sneppx[-_]alg/i
const WORKFLOW = /\.github\/workflows|workflows\//

export default (async () => ({
  "tool.execute.before": async (input, output) => {
    if (input.tool !== "bash") return
    const cmd = String(output.args?.command ?? "")
    if (!WORKFLOW.test(cmd)) return
    if (!SNEPPX_ALG.test(cmd)) return

    throw new Error(
      "SneppX policy: CI/CD workflow files are not allowed in sneppx-alg " +
        "(no local toolchain, no CI). Verify with per-file pytest or cmake."
    )
  },
})) satisfies Plugin
