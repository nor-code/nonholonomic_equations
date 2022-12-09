import re

first_regexp = {
              r'Derivative[\(]x[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x, t), t)',
              r'Derivative[\(]y[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(y, t), t)',
              r'Derivative[\(]α[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x1, t), t)',
              r'Derivative[\(]β[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x2, t), t)',
              r'Derivative[\(]γ[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x3, t), t)',
              r'Derivative[\(]φ[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x4, t), t)',
              r'Derivative[\(]ψ[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x5, t), t)',
              r'Derivative[\(]δ[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x6, t), t)',
              r'Derivative[\(]ε[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x7, t), t)',
              r'Derivative[\(]τ[\(]t[\)], [\(]t, 2[\)][\)]': 'diff(diff(x8, t), t)',
              r'Derivative[\(]x[\(]t[\)], t[\)]': 'diff(x, t)',
              r'Derivative[\(]y[\(]t[\)], t[\)]': 'diff(y, t)',
              r'Derivative[\(]α[\(]t[\)], t[\)]': 'diff(x1, t)',
              r'Derivative[\(]β[\(]t[\)], t[\)]': 'diff(x2, t)',
              r'Derivative[\(]γ[\(]t[\)], t[\)]': 'diff(x3, t)',
              r'Derivative[\(]φ[\(]t[\)], t[\)]': 'diff(x4, t)',
              r'Derivative[\(]ψ[\(]t[\)], t[\)]': 'diff(x5, t)',
              r'Derivative[\(]δ[\(]t[\)], t[\)]': 'diff(x6, t)',
              r'Derivative[\(]ε[\(]t[\)], t[\)]': 'diff(x7, t)',
              r'Derivative[\(]τ[\(]t[\)], t[\)]': 'diff(x8, t)',
              r'Derivative[\(]x[\(]t[\)], t[\)] [*][*] 2': 'diff(x, t)**2',
              r'Derivative[\(]y[\(]t[\)], t[\)] [*][*] 2': 'diff(y, t)**2',
              r'Derivative[\(]α[\(]t[\)], t[\)] [*][*] 2': 'diff(x1, t)**2',
              r'Derivative[\(]β[\(]t[\)], t[\)] [*][*] 2': 'diff(x2, t)**2',
              r'Derivative[\(]γ[\(]t[\)], t[\)] [*][*] 2': 'diff(x3, t)**2',
              r'Derivative[\(]φ[\(]t[\)], t[\)] [*][*] 2': 'diff(x4, t)**2',
              r'Derivative[\(]ψ[\(]t[\)], t[\)] [*][*] 2': 'diff(x5, t)**2',
              r'Derivative[\(]δ[\(]t[\)], t[\)] [*][*] 2': 'diff(x6, t)**2',
              r'Derivative[\(]ε[\(]t[\)], t[\)] [*][*] 2': 'diff(x7, t)**2',
              r'Derivative[\(]τ[\(]t[\)], t[\)] [*][*] 2': 'diff(x8, t)**2'
}

second_regexp = {
    r'x[\(][t][\)]': 'x',
    r'y[\(][t][\)]': 'y',
    r'α[\(][t][\)]': 'x1',
    r'β[\(][t][\)]': 'x2',
    r'γ[\(][t][\)]': 'x3',
    r'φ[\(][t][\)]': 'x4',
    r'ψ[\(][t][\)]': 'x5',
    r'δ[\(][t][\)]': 'x6',
    r'ε[\(][t][\)]': 'x7',
    r'τ[\(][t][\)]': 'x8'
}


def transform_to_simpy(row):
    for key in first_regexp.keys():
        row = re.sub(re.compile(key), first_regexp[key], row)

    for key in second_regexp.keys():
        row = re.sub(re.compile(key), second_regexp[key], row)

    return row
