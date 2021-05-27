# Valid Phone Numbers

[Leetcode problem](https://leetcode.com/problems/valid-phone-numbers/)

## Description

Given a text file `file.txt` that contains a list of phone numbers (one per
line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two
formats (`x` means a digit):

- `(xxx) xxx-xxxx`;
- `xxx-xxx-xxxx`.

You may also assume each line in the text file must not contain leading or
trailing white spaces.

## Examples

`file.txt`:

```
987-123-4567
123 456 7890
(123) 456-7890
```

The script would return:

```
987-123-4567
(123) 456-7890
```

## Driver code instructions

```
bash solution.sh
```

Or, if there is `x` permission and you're logged into `bash`:

```
./solution.sh
```
