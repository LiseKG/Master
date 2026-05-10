
Introduction: In software engineering, bad code can be categorized into code smells. We will focus on three code smells; God class, Long Methods and Feature Envy. The goal is to generate two files for each code smell. One smelly and one refactored version without the smell. 

Input:
Generate two Python files per code smell: one containing the smell and one refactored version. In total you should have 6 python files. Try to focus on one code smell and avoid creating overlap with smells in the files. Both versions (refactored and smelly) should implement the same functionality (e.g., a simple order processor, calculator, or student records manager). The files do not have to have the same functionality across the different pairs of code smell files. 

Use "trading" as the domain context. All classes, methods, functions, and test cases should be thematically related to this topic.

Context:
1. God class
The definition of  god class is when a huge class which is surrounded by many data classes acts as a controller. The god class centralizes and is responsible for most decision taking.
- Make sure the "god class" class has more than 20 methods.
- The files should avoid having the code smells feature envy or long methods.

2. Feature envy
The definition of "Feature Envy" is when a method seems more interested in another class. We redefine Feature Envy to be a standalone function excessively using the attributes/methods of another class. 
- The function should call attributes of another class more than 5 times. This can be calling a class with class.item. 
- Do not place this class inside any class.
- The files should avoid having the code smells god class or long methods.

3. Long methods
The definition of "Long method" is when a method performs more than one operation and has a length of more than 30 lines.
- Long methods code smells must be more than 30 lines.
- The files should avoid having the code smells god class or feature envy.
- Do not place this method inside another class.

Output:
The output should be six Python files, 3 refactored versions and 3 smelly versions. Output each file as a separate code block labelled “File <codesmell> smelly version: <codesmellname>_<version>.py” and the refactored files as “File <codesmell> refactored version: <codesmellname>_<version>_RF.py”.
The current version is {version}.  The codesmellsnames are either godclass, longmethod or featureenvy.

Rules for all files:
Do not use imports. 
All files must be syntactically valid and runnable.
The methods inside the files should not start with _ (underscore). The only exception is the method __init__. 
The two files should contain a test at the bottom of each file that prints or asserts expected values. 
The test must test the same functionality across both versions (smelly and refactored) and observe the same output. 


### Feature envy prompt

Introduction: In software engineering, bad code can be categorized into code smells. Focus on creating one file containing the smell feature envy.

Input:
Generate one Python files. Try to focus on making a code file that contains feature envy and avoid creating overlap with other code smells. 

Use this interface for creating the structure of the file. interface: {int_content} 
Context:
1.  Feature envy
The definition of "Feature Envy" is when a method seems more interested in another class. We redefine Feature Envy to be a standalone function excessively using the attributes/methods of another class. 
The method does not have to be in the interface.
The smelly file should contain:
- Ons standalone function (not inside any class) that excessively uses another class's attributes or methods.
- The standalone function must call attributes of another class more than 10 times.
- Each explicit reference in the source code counts as one occurrence, regardless of loops or runtime execution
- Attribute or method access must be written explicitly (e.g., object.attribute)
- The function must not be placed inside any class
- The files should avoid having the code smells god class or long methods.


Output:
The output should be one Python file with a comment at the top saying “#File featureenvy smelly version: featureenvy_{version}_s.py”. 

Rules for all files:
Do not use imports. 
All files must be syntactically valid and runnable.
The methods inside the files should not start with _ (underscore). The only exception is the method __init__. 

### Long method

Introduction: In software engineering, bad code can be categorized into code smells. Focus on creating one file containing the smell long method.

Input:
Generate one Python files. Try to focus on making a code file that contains long method and avoid creating overlap with other code smells. 

Include the class(es) defined in this interface in the file: {int_content}.
If you add any new methods, one of the methods in the interface must call the new method.
The long method MUST be a standalone function defined at module scope.
It MUST NOT be defined inside any class, including any class from the interface.
At least one class from the interface MUST CALL the long method,but the long method itself MUST remain outside all classes.


Context:
1. Long methods
The definition of "Long method" is when a method performs more than one operation and has a length of more than 30 lines.
- One method MUST contain at least 30 NON-BLANK, NON-COMMENT, executable lines.
Each line must contain a statement (no pass, no ellipsis).
- The files should avoid having the code smells long method or feature envy.
- Do not place the long method method inside a class. The long method should be a standalone method.

Enforcement for smelly version:
- EXACTLY one function must be the long method.
- Only executable statements inside the long method body may be numbered.
- Numbering must start at #1 on the first executable statement inside the method.
- Numbering must increase sequentially and end inside the same method.
- The highest number inside the method MUST be at least #35.
- Each numbered line MUST be a distinct executable statement (assignment, condition, loop operation, or mutation).
- The model MUST continue adding logically redundant but executable steps until at least #35 is reached.
- Numbering is required only for the smelly version.
- Do not count comments


Rules for all files:
Do not use imports. 
All files must be syntactically valid and runnable.
The methods inside the files should not start with _ (underscore). The only exception is the method __init__. 

Output:
The output should be one Python file with a comment “#File longmethod smelly version: longmethod_{version}_s.py” then the python code.

###  God class


Introduction: In software engineering, bad code can be categorized into code smells. Focus on creating one file containing the smell god class.

Input:
Generate one Python files. Try to focus on making a code file that contains god class and avoid creating overlap with other code smells. 

Use this interface for creating the structure of the file. interface: {int_content}

The definition of  god class is when a huge class which is surrounded by many data classes acts as a controller. The god class centralizes and is responsible for most decision taking.
- Make sure the "god class" class has more than 20 methods.
- Number each method with a number until you reach 20.
- The files should avoid having the code smells feature envy or long methods.
- All methods must be relevant and be called on atleast once. Methods can call each other. 
- A method must contain more than pass and a comment.
- The god class should be one of the classes mentioned in the interface

In the interface there are some defined method names. All methods in the smelly files must be called by one method in the interface or a method thats called by another metod in the interface.

At the bottom of the file add a if __name__ = '__main__' that test all methods used in the file.

Rules for all files:
Do not use imports. 
All files must be syntactically valid and runnable.
The methods inside the files should not start with _ (underscore). The only exception is the method __init__. 

Output:
The output should be one Python file with a comment “#File godclass smelly version: godclass_{version}_s.py”. 

### test files

Context: Test cases for a Python program. Generate a single Python test file that tests multiple implementations
of the same interface.

ALL business rules, class names, constructor signatures, and method names MUST be taken exclusively from the provided interface.
Do NOT restate, redefine, or invent any rules, classes, or methods.

Interface:
{int_content}

Test cases are found as a comment in the interface.

Import each file as X import "all classes" as Y,Z.... The classes we want to import are found in the interface. Do not import any other class 
- godclass_{version}_s.py
- godclass_{version}_s_RGC.py
- godclass_{version}_s_RGC_E.py
- longmethod_{version}_s.py
- longmethod_{version}_s_RLM.py
- longmethod_{version}_s_RLM_E.py
- featureenvy_{version}_s.py
- featureenvy_{version}_s_RFE.py
- featureenvy_{version}_s_RFE_E.py


Testing rules:
Detect and use ONLY the classes defined in the interface
- Instantiate each class using the constructor defined in the interface
- Use only the buisness rules in the interface to create test. Do not invent or restate any requirments.
- Assert to check if the the returned value contains the expected result. This does not have to be strictly the same as long as it contains the value.

Execution rule:
- Use a loop to run all test cases against all implementations
- Clearly print which file and class is being tested

Output:
The output should be one Python file labelled “#File testsmell test version: test_<version>.py”. The current version is {version}. 


### Refactor Feature envy: (last version)

Introduction: In software engineering, bad code can be categorized into code smells. We will focus on removing the code smells called feature envy. 

Input:
I am providing you a smelly python file  and you must only remove the feature envy code smell. 
The fixed files must the same functionality same output as the original file provided. 
Do not change the class names unless needed for removing the code smell.
smelly files: {scontent}

Do not remove any of the methods or classes provided in this interface: {int_content}

Context:
1.  Feature envy
The definition of "Feature Envy" is when a method seems more interested in another class. We redefine Feature Envy to be a standalone function excessively using the attributes/methods of another class. 

Feature envy elements are counted by:
- Each explicit reference in the source code counts as one occurrence, regardless of loops or runtime execution
- Attribute or method access must be written explicitly (e.g., object.attribute, object.method())
- The fixed function must not be placed inside any class

You must move and divide the feature envy method to remove the code smell. You must make sure none of methods are envy of another class.
You can do this by splitting or moving functionality. You can not change the console output or functionality of the program.

Rules for the file:
Do not use imports. 
All files must be syntactically valid and runnable.
The methods inside the files should not start with _ (underscore). The only exception is the method __init__. 

If the file contains tests, you are allowed to change the test as long as output to the console remains the same.

Output:
The output should be one Python file starting with a comment  “#File featureenvy refactored version: {filename}_RFE.py”

### Refactoring God class (last version)

Introduction: Focus on removing the code smells called god class. 

smelly files {scontent}
Interface: {int_content}

Detect a god class using this rule: Any class with more than 20 methods. 
The new file MUST not have any classes with more than 19 methods.
Refactor strategy:
- if two method differ only by constant values (drive_to_work, drive_to_home) combine them into a single method that accepts a parameter.
- Move method that operate on similar data into the same new class.

Interface preservation rules:
- All public method defined in the provided interface must still exist with the same names and parameters.
- These methods may delegate internally but must preserve: Same return values, same printed output and same side effects.

Behavioral Equivalence Rule:
The refactored file must produce byte-for-byte identical printed output.
All assertions in the test section must still pass.
No logic may be removed — only relocated.

Structural Constraints:
No class may contain more than 20 methods after refactoring. 
If a class contains more than 20 methods, split it into multiple classes.
No method may contain only pass or comments.
No imports allowed.
The if __name__ == "__main__" block must remain functionally identical.
Output Format:
Output exactly one valid Python file.
Start with:

#File godclass refactored version: {filename}_RGC.py

Remove smells from the smelly file.

### Refactoring Long methods (last version)
Introduction:
In software engineering, bad code can be categorized into code smells.
We will focus only on removing the code smell called "Long Method".

Input:
I will provide a smelly Python file:{scontent}
You must refactor it to remove ONLY the Long Method smell.
Interface for structure {int_content}

Definition:
A method or function is considered a Long Method if it contains
30 or more NON-BLANK, NON-COMMENT, executable lines.

Refactoring Constraints:

1. Scope of Refactoring
- You may ONLY refactor methods/functions that qualify as Long Methods.
- You may split a long method/function into smaller helper methods/functions.
- You may delegate logic to newly created helper methods/functions.
- You may NOT refactor methods that are not long.

2. Function and Method Preservation
- All existing classes must remain.
- All existing methods must remain with the SAME Name, Parameters and Return values.
- No existing function or method may be deleted.
- No existing function or method may be renamed.
- The body of a long method may delegate to helpers, but the original method/function must still exist.

3. Call Graph Preservation
- All original function and method calls must remain in the same locations.
- No call may be removed.
- No call may be moved to another scope.
- The number of times each function executes in the test must remain identical.

4. Behavioral Equivalence (Strict)
- The refactored program must produce byte-for-byte identical console output.
- All print statements must produce exactly the same text in the same order.
- All side effects must remain identical.
- All return values must remain identical.
- No logic may be removed — only relocated.

5. Test Section Rules
- The structure of the test section must remain similar to the original.
- You may not remove or add function calls.
- You may not remove execution of any existing function.
- The observable behavior of the test must remain identical.

6. Code Restrictions
- Do not use imports.
- The file must be syntactically valid and runnable.
- Methods must not start with "_" except for "__init__".
- You may create additional helper methods/functions, but they must follow the same naming rule.

7. Reuse of Logic
- When splitting a long method, reuse existing functionality whenever possible.
- Do not duplicate logic that already exists elsewhere in the file.

Output Format:
Return exactly ONE Python file.
The file must start with this exact comment:

#File longmethod refactored version: {filename}_RLM.py

Do not include explanations.
Only output the final refactored Python file.

### Refactoring for Energy
Introduction:
I am using these files as a demonstration of different coding behaviours. Improve energy usage by removing any energy inefficiencies.

Context / Goal:
Refactor the code to improve readability, maintainability, and energy efficiency, without changing program behaviour.
Here is an interface: {int_content} 
All classes and methods listed in the interface MUST remain present in the output. 
Their names, input-parameters, output MUST NOT change. 

Here is the file you should refactor: {scontent}

Preservation Rules
Do not change the program's logic or outcome.
Preserve function and variable names unless renaming improves clarity and efficiency.
Do not remove needed methods and variables for the programs logic and calculations.
Maintain the same input/output behaviour.

Energy-Efficient Refactoring
Reduce unnecessary CPU usage.
Eliminate redundant loops, repeated calculations.
Replace inefficient patterns with optimized alternatives.
Prefer built-in, vectorized, or library-optimized functions when appropriate.
Minimize excessive I/O operations.
Avoid unnecessary object creation and memory churn.
Improve data access patterns and caching where beneficial.

Prioritize changes that reduce execution time and hardware utilization, even if they slightly increase code complexity, as long as readability is preserved.

Output:
The output should be one Python file starting with a comment  “#File energy refactored version: {filename}_E.py”