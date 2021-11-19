"""
Code the logic of RISK strategy board game in case of two players. The attacker rolls 3 red
dices and the defender rolls 2 blue dices. In step one, we look for the greatest value in the
dices. The looser loses 1 soldier. If the greatest value is the same at both sides, only the
attacker loses 1 soldier. In step two, we look for the second greatest value and decide about
losing 1 soldier as above. The game has 3 possible outcomes:
 - attacker loses 2 soldiers represented with value 1
 - both sides lose 1 soldier each represented with value 2
 - the defender loses 2 soldiers represented with value 3

a) Simulate the game 1000 times and calculate the relative frequency of the three possible outcomes.
b) Simulate the game 1000000 times and calculate the relative frequency of the three possible outcomes.
c) Calculate the exact probability of the three outcomes by analyzing all possible cases (positive cases / all cases).

Print out the results of tasks a, b and c in a tabular form.
            Attacker Both Defender
1000 turns: 0.35222 0.44444 0.20334
1000000 turns: 0.33988 0.43011 0.23001
Probability: 0.34000 0.43000 0.23000
"""
import numpy as np
import numpy.random as rd


def start_risk_game(trails: int = 1):
    # print('running %s trail(s)' % trails)
    result = np.empty(0, int)
    for _ in range(trails):
        # the attacker rolls 3 red dices
        red_dices = rd.choice([1, 2, 3, 4, 5, 6], size=(1, 3), p=(1/6, 1/6, 1/6, 1/6, 1/6, 1/6))
        # print('red dices are', red_dices)
        # the defenders rolls 2 blue dices
        blue_dices = rd.choice([1, 2, 3, 4, 5, 6], size=(1, 2), p=(1/6, 1/6, 1/6, 1/6, 1/6, 1/6))
        # print('blue dices are', blue_dices)
        # the below for loop represents the 2 steps
        for _ in range(2):
            max_red = np.max(red_dices)
            max_blue = np.max(blue_dices)
            # print(max_red, max_blue)
            if max_red > max_blue:
                indx_max_blue_dice = np.argmax(blue_dices == max_blue)
                blue_dices = np.delete(blue_dices, indx_max_blue_dice)
            else:
                indx_max_red_dice = np.argmax(red_dices == max_red)
                red_dices = np.delete(red_dices, indx_max_red_dice)
            # print('red dices are', red_dices)
            # print('blue dices are', blue_dices)
        result = np.append(result, red_dices.size)
    return result


if __name__ == '__main__':
    print(f"{' ':18}{'Attacker':12}{'Both':12}{'Defender':12}")
    run_times = [1000, 10000, 100000]
    for t in run_times:
        results = start_risk_game(t)
        uniq_arr, cnts = np.unique(results, return_counts=True)
        # print(uniq_arr, cnts)
        # the relative frequency of the three possible outcomes
        r_f = np.divide(cnts, t)
        print(f"{str(t)+' turns:':12}{r_f[np.where(uniq_arr == 1)[0][0]] if 1 in uniq_arr else 0:12}"
              f"{r_f[np.where(uniq_arr == 2)[0][0]] if 2 in uniq_arr else 0:12}"
              f"{r_f[np.where(uniq_arr == 3)[0][0]] if 3 in uniq_arr else 0:12}")

