statuses = {
    20: '🚃',
    10: '🚋',
    30: '🚞',
    90: '🚝',
    100: '🚄',
    80: '🚅',
    70: '🚈',
    0: '🚂',
    110: '🚆',
    60: '🚇',
    50: '🚊',
    40: '🚉',
}


def get_status(score: int) -> str:
    for key in sorted(statuses.keys(), reverse=True):
        if score >= key:
            return statuses[key]
    return statuses[0]
