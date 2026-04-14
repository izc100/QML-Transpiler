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

Elijah - I learned about parsing and lexing, as well as building the abstract syntax tree in python. I did not experience any roadblocks in my work. Overall the project was fun and not too difficult.

Isaac - I mostly handled documentation, git workflow, and integration. I did not handle the language as much but I got to see the end result and how it works. The biggest thing I did see was how the transplier is not only three separate programs but if the token format or structure drifts between stages, everything breaks in subtle ways until you test end-to-end. Everyone worked really fast and well together, so there were no problems with communication. I found looking over everything to be a little difficult, just took time. 

Andrew - I designed and implemented the recursive-descent parser and wrote its initial test suite. Building the parser required carefully translating EBNF grammar rules into dedicated methods while enforcing structural constraints — such as minimum option counts and non-empty fields — directly at parse time. Writing the tests alongside the parser helped me catch edge cases early and strengthened my understanding of how recursive-descent parsing and error handling work in practice.​​​​​​​​​​​​​​​​

### Member 1
Brandon Hoggatt

### Member 2
Isaac Chapman

### Member 3
Elijah Reyna

### Member 4
Andrew Benyacko
