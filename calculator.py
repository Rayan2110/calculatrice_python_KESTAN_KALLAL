# 
import re
class Calculator:


    _TOKEN_REGEX = re.compile(r'\d+\.\d+|\d+|[+\-*/()]')

    def evaluate(self, expression: str) -> float:
       
        tokens = self._tokenize(expression)
        rpn = self._to_rpn(tokens)
        return self._eval_rpn(rpn)

    def _tokenize(self, text: str) -> list[str]:
      
        cleaned = text.replace(' ', '')
        return self._TOKEN_REGEX.findall(cleaned)

    def _to_rpn(self, tokens: list[str]) -> list[str]:
       
        precedence = {'+': 1, '-': 1, '*': 2}
        output_queue = []
        operator_stack = []

        for tok in tokens:
            if re.fullmatch(r'\d+\.\d+|\d+', tok):
                output_queue.append(tok)

            elif tok in precedence:
                while (operator_stack and
                       operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[tok]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(tok)

            elif tok == '(':  
                operator_stack.append(tok)

            elif tok == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()  

            else:
                raise ValueError(f"Unknown token: {tok}")

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return output_queue

    def _eval_rpn(self, rpn_tokens: list[str]) -> float:
      
        stack: list[float] = []

        for tok in rpn_tokens:
            if re.fullmatch(r'\d+\.\d+|\d+', tok):
                stack.append(float(tok))
            else:
                right = stack.pop()
                left = stack.pop()

                if tok == '+':
                    result = left + right
                elif tok == '-':
                    result = left - right
                elif tok == '*':
                    result = left * right
                else:
                    raise ValueError(f"Unsupported operator: {tok}")

                stack.append(result)

        if len(stack) != 1:
            raise ValueError("Malformed expression.")
        return stack[0]



if __name__ == "__main__":
    calc = Calculator()
    examples = [
        "2 + 3 * 4",
        "10 - 2 * 3 + 5",
        "3.5 * 4 - 1.5",
        " ( 6 + 2 ) * 3 ",  
    ]
    for expr in examples:
        print(f"{expr} = {calc.evaluate(expr)}")


