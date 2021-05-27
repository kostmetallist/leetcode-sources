# Leetcode sources

Storage for my solutions to problems posted on [Leetcode](https://leetcode.com)
portal.

<p align="center">
  <img width="85%" src="@pic/leetcode.png" />
</p>

## Structure

Each problem has a corresponding root-level catalog named exactly as the
problem on the site.

If there is more than one solution per task, then `v1`, `v2`, etc. subcatalogs
are placed under problem's directory. In case solutions are presented in
different programming languages, self-descriptive names can be given, like
`c++` and `java`. Multiple solutions on the same language combine notation
rules described above.

For instance, if there is a problem called `tradesperson-polynomial-algo`, and
there are two implementations on `c++` and one on `java`, the layout must be
similar to this:

```
tradesperson-polynomial-algo
|_ c++_v1
|_ c++_v2
|_ java
```

On the problem catalog level, two files must be present: `README.md` and a
solution one.

Readme should contain the following elements:

- link to the original problem on Leetcode
- textual description of the task
- [optionally] example(s) of input and expected output
- [optionally] instructions to run driver code

Solution file format depends on chosen language and is named according to
common style for that language (e.g. `Solution.java` but `solution.py`). This
file contains logic required by task statement. Solution must contain only code
for submission.

There can also be a driver code to run solution in a separated class/script/etc.
It should import data structures and functions from solution file and perform
some operations showing that the task solved correctly.

## Contributions

Every Leetcode problem is assigned a unique number. Solutions are supposed to
be provided via separate branches. Squashing is required before merging into
`master`. Branch name convention: `LC-<problem_number>`.

## Comments/suggestions

The repo holds my personal solutions, and I target at some kind of independent
thought process. Nevertheless, you are free to post any ideas to improve
existing implementations on
[Issues](https://github.com/kostmetallist/leetcode-sources/issues) page.
