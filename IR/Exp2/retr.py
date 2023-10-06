import csv

# Function to read the inverted index from a CSV file
def read_inverted_index(filename):
    inverted_index = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            termid = int(row[0])
            docids = list(map(int, row[1].split()))
            if termid not in inverted_index:
                inverted_index[termid] = docids
            else:
                inverted_index[termid].extend(docids)
    return inverted_index

# Function to perform AND operation between two lists
def perform_and(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return result

# Function to perform OR operation between two lists
def perform_or(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

# Function to evaluate a Boolean expression
def evaluate_expression(expression, inverted_index):
    stack = []
    terms = expression.split()
    
    for token in terms:
        if token.isdigit():
            # Token is a termid, convert it to an integer
            termid = int(token)
            stack.append(inverted_index.get(termid, []))
            # print(f'token : {termid}, list : {stack[-1]}')
        elif token.upper() == 'AND':
            if len(stack) < 2:
                raise ValueError("Not enough operands for AND operation")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_and(operand1, operand2)
            stack.append(result)
        elif token.upper() == 'OR':
            if len(stack) < 2:
                raise ValueError("Not enough operands for OR operation")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_or(operand1, operand2)
            stack.append(result)
        else:
            raise ValueError("Invalid token: {}".format(token))

    # After processing all tokens, the stack should contain the final result
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]

# Function to convert a Boolean query to postfix notation
def infix_to_postfix(query):
    precedence = {'AND': 1, 'OR': 2}
    output = []
    stack = []

    for token in query.split():
        if token.isdigit():
            output.append(token)
        elif token in ('AND', 'OR'):
            while (stack and stack[-1] in ('AND', 'OR') and
                   precedence[token] <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
    
    while stack:
        output.append(stack.pop())

    return ' '.join(output)


try:
    # Example Boolean expression
    inverted_index_filename = 'inverted_index.csv'
    inverted_index = read_inverted_index(inverted_index_filename)
    boolean_expression = infix_to_postfix("2 OR 3")
    result = evaluate_expression(boolean_expression, inverted_index)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

