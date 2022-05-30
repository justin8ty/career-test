---
aliases:
tags:
crafted: Friday 2022-04-01
refined: Saturday, 2022-04-02
---

# ENGFF019 Career Test Testing Methodology

Co-Authored by:

Names: Anthony Saopa Phiri | Tan Jin Yi

Student IDs: 20401485 | 20396553

## Mission

The following document outlines our testing methodology for **ENGFF019**'s Python pair programming assessment.

## Table of Contents

```toc

```

## Test Data

---

### `mainModule.py`

#### `nameInput()`

We did not implement error checking for the `name`, as some users may prefer to stay anonymous and provide usernames containing numbers or special characters instead.

| firstName | lastName | name          |
| --------- | -------- | ------------- |
| 6lack     | the1     | 6lack the1    |
| Joseph    | Martin   | Joseph Martin |
| Travish   | 666      | Travish 666   |

#### `programStart()`

| startTest | Behavior / Output                                                       |
| --------- | ----------------------------------------------------------------------- |
| 0         | `Thanks for using our service. Have a nice day!` and program terminates |
| 1         | `Instructions: Enter (1) if you agree. Enter (0) if you disagree.`      |
| 3         | `Please enter (1) to start the test, or (0) to end your session:`       |
| A         | `Invalid literal for int() with base10` and program terminates          |

#### `programRestart()`

| enterRestart | Behavior / Output                                                 |
| ------------ | ----------------------------------------------------------------- |
| 9c           | Program will not execute further until ENTER key is pressed.      |
| 9c + ENTER   | `Please enter (1) to start the test, or (0) to end your session:` |
| ENTER        | `Please enter (1) to start the test, or (0) to end your session:` |

---

### `careerQuestions.py`

All the `*Input()` functions here contain nearly identical code, but interact with different variables.

#### `creativeInput()`

| creativeChoice1                                              | creativeChoice2 | creativeChoice3                                                    | creativeChoice                          |
| ------------------------------------------------------------ | --------------- | ------------------------------------------------------------------ | --------------------------------------- |
| 1                                                            | 0               | 1                                                                  | 2                                       |
| 3 (`Please enter (1) if you agree, or (0) if you disagree.`) | 1               | 0                                                                  | Depends on creativeChoice1’s final data |
| 0                                                            | 1               | K (`Invalid literal for int() with base10` and program terminates) | -                                       |

#### `stemInput()`

| stemChoice1 | stemChoice2                                                  | stemChoice3                                                        | stemChoice                          |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------------ | ----------------------------------- |
| 0           | 1                                                            | 1                                                                  | 2                                   |
| 1           | 9 (`Please enter (1) if you agree, or (0) if you disagree.`) | 1                                                                  | Depends on stemChoice2’s final data |
| 0           | 0                                                            | H (`Invalid literal for int() with base10` and program terminates) | -                                   |

#### `laborInput()`

| laborChoice1 | laborChoice2                                                 | laborChoice3                                                       | laborChoice                          |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------ |
| 0            | 0                                                            | 0                                                                  | 0                                    |
| 1            | 3 (`Please enter (1) if you agree, or (0) if you disagree.`) | 1                                                                  | Depends on laborChoice2’s final data |
| 0            | 0                                                            | D (`Invalid literal for int() with base10` and program terminates) | -                                    |

---

### `careerResults.py`

No test data needed, as this module does not accept any explicit user inputs from the terminal interface. Test run screenshots are provided below.

---

## Test Runs

---

### `mainModule.py`

#### `nameInput()`

This function should accept any data.

![](https://i.imgur.com/7kRxLPJ.png)

Refer to [[#Test Runs#careerResults py]] for more name data samples.

#### `programStart()`

This run uses invalid data:

![](https://i.imgur.com/R1GS3PW.png)

![|1100](https://i.imgur.com/qfFcs8w.png)

This run uses valid data:

![](https://i.imgur.com/XirYo9e.png)

#### `programRestart()`

Explicitly terminated:

![](https://i.imgur.com/qFLwd2m.png)

Explicitly continued:

![](https://i.imgur.com/3llHd0x.png)

---

### `careerQuestions.py`

#### `creativeInput()`

![](https://i.imgur.com/uPyMe4f.png)

#### `stemInput()`

![|1100](https://i.imgur.com/AH1jzvb.png)

#### `laborInput()`

![|1100](https://i.imgur.com/PaWxsNE.png)

---

### `careerResults.py`

#### `careerOutput1()`

![|1100](https://i.imgur.com/gPnOPFo.png)

#### `careerOutput2()`

![|1100](https://i.imgur.com/KXuhCB6.png)

#### `careerOutput3()`

![|1100](https://i.imgur.com/SPiBFpa.png)

#### `careerOutput4()`

![|1100](https://i.imgur.com/P3CdhMn.png)

## Complete Test Run in Windows Terminal

1st page:

![](https://i.imgur.com/4HIrfNq.png)

2nd page:

![](https://i.imgur.com/2RuFswO.png)

---
