from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):

    points_of_winning = difficulty * 3 + 5

    try:
        with open(SCORES_FILE_NAME, 'r') as score_file:
            current_score = int(score_file.read())
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + points_of_winning

    try:
        with open(SCORES_FILE_NAME, 'w') as score_file:
            score_file.write(str(new_score))
    except IOError:
        return BAD_RETURN_CODE

    return new_score


