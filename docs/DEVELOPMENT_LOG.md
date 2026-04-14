# QML Transpiler — Development Log

A living document tracking the project from day one. Update regularly, not at the last minute. 

---

## Meeting Summaries

| Date | Attendees | Outcome |
|------|-----------|---------|
| 2026-03-12 | Brandon Hoggatt, Isaac Chapman, Elijah Reyna, Andrew Benyacko | **Online kickoff:** split up project rules and the QML schema expectations; **agreed on EBNF** for the language; **chose Python** for the implementation; divided work across lexer, parser, serializer, and tests so modules could be built in parallel. |
| Post 3/12 — submission (async) | Full team (Discord) | **No further formal meetings.** Questions and clarifications (integration, token format, parser expectations, bugs) were handled **asynchronously on Discord**; we aligned again informally near the end for tests, fixes, and submission polish. |


---

## Task Delegation

| Area | Primary owner | Scope |
|------|---------------|--------|
| **Lexer (Part 2)** | Brandon Hoggatt | Regex-based scanner in `src/lexer/`; token list contract for the parser; lexer-focused tests. |
| **Parser (Part 3)** | Andrew Benyacko | Recursive-descent parser in `src/parser/`; nested quiz structure and syntax errors; parser-focused tests. |
| **Serializer / generator (Part 4)** | Elijah Reyna | JSON output in `src/generator/`; wiring parser output to `json` dump; serializer-focused tests. |
| **Documentation, integration, Git** | Isaac Chapman | README and development log; end-to-end wiring (e.g. `main.py` invoking lexer → serializer); branches/merges and keeping the repo consistent for the team. |

**Tests:** Each milestone owner drove tests for their stage; Isaac focused on integration and keeping the full pipeline runnable as pieces landed.

---

## Design Decisions & Roadblocks

### Design decisions
- The team used a regex-based lexer with named capture groups so token matching stayed modular and easy to extend.
- We kept a strict token contract (`(token_type, token_value)`) between lexer and parser so both modules could be developed in parallel.
- The parser was implemented as recursive descent to map directly to the EBNF grammar and produce clearer syntax errors.
- JSON was chosen as the final output format to match project needs and simplify serialization and testing.

### Roadblocks
- Brandon - debugged issue where regex pattern was not accurately capturing the bad input, and was only including the first character - 3/13/2026.
- Andrew - resolved parser edge cases where invalid structure (missing close tags or not enough options) needed clearer "expected vs found" errors during recursive parsing.
- Elijah - fixed serializer integration issues by ensuring parser output shape stayed consistent before JSON dumping, which avoided downstream key/structure mismatches in output tests.
- Isaac - handled integration and CLI wiring issues (`main.py`, default output behavior, and test-run workflow consistency) so the full pipeline ran reliably from the repo root.

---

## Individual Reflections

*Each team member adds a 1-paragraph reflection at the end of the project.*

### Member 1
Brandon Hoggatt

### Member 2
Isaac Chapman

### Member 3
Elijah Reyna

### Member 4
Andrew Benyacko
