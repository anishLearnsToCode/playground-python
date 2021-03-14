from typing import Dict, List, Tuple


def optimal_block(blocks: List[Dict[str, bool]], requirements: List[str]) -> int:
    scores: List[Tuple[int, int]] = []
    requirements = requirements[::-1]
    for index, block in enumerate(blocks):
        score = 0
        for i, requirement in enumerate(requirements):
            score += int(block[requirement]) * (2 ** i)
        scores.append((index + 1, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]


print(optimal_block(blocks=[
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": False}],
    requirements=['gym', 'school', 'store'])
)
