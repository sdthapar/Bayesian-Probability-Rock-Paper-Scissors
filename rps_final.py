import sys
import random
import math

def main():



    def patgen(k,x):
        # Generates all possible combinations of previous k entries and adds them to the dictionary of dictionaries
        lst = ['0','1','2']
        d = ['0','1','2']
        for i in range(0,k-1):
            f = []
            for i in range(0,len(lst)):
                a = lst[i]
                for j in range(0,3):
                    str = a + d[j]
                    f.append(str)
            lst = f
        # print(lst)
        for key in x:
            # Gets dictionary for each key in x
            for n in range(0, len(lst)):
                    # Makes entries for each combination
                x[key][lst[n]] = 0.1

        return x


    k = sys.argv[1]
    k = int(k) # past k inputs that we need to consider
    c = 0
    ctr = 1
    input_moves = []
    # copy_moves = input_moves[0:len(input_moves)-1] # list of player moves for conditioning
    terminal_output = []
    zero_k = [0,0,0]
    prev_zk = [0,0,0]
    b = True
    while b == True:
        r = raw_input()
        r = int(r)

        input_moves.append(r)

        copy_moves = input_moves[0:len(input_moves)-1]

        x = dict() # Dictinary containing the moves with dictionary of previous moves as values
        x[0] = dict()
        x[1] = dict()
        x[2] = dict()
        if k == 0:
            # When k is zero we just calculate the count for the opponent moves and play the move which can defeat the move with highest count
            zero_k[r] = zero_k[r] + 1

            m = max(prev_zk)


            ind = prev_zk.index(m)


            if ind == 0:
                print(str(1))
            elif ind == 1:
                print (str(2))
            elif ind == 2:
                print(str(1))


        elif k >= len(copy_moves):
            # We play random until we have enough past history to start calculating the probabilities
            luck = random.randint(0,2)
            terminal_output.append(luck)
            print(str(luck))
        elif k < len(copy_moves):
            x = patgen(k,x) # Initializes the dictionary x with the right values according to k and sets them to 0.1

            c = math.pow(3,k)
            normalizer = c*0.1
            for i in range(0,len(copy_moves)):

                if i+k < len(copy_moves):
                    key2 = ''.join(str(x) for x in copy_moves[i:i+k])

                    key1 = copy_moves[i+k]

                    last_val = x[key1][key2]
                    x[key1][key2] = last_val+1 # This updates the count for every move given past k moves


            for key in x:
                for v in x[key]:
                    if x[key][v] != 0.1:

                        l_val = x[key][v]
                        base = copy_moves[0+k:].count(key)
                        x[key][v] = l_val/(base + normalizer) # This divides the counts to calculate the probabilities, it also normalizes at the same time



            last_k_input = ''.join(str(x) for x in copy_moves[len(copy_moves)-k:]) # This builds a string of the past k inputs


            inter_res = [] # This will contain final probabilities before normalizing

            for key in x:

                p_key = round(copy_moves.count(key), 3)/len(copy_moves)
                p_key = round(p_key, 3)

                conditional_key = x[key][last_k_input] # This takes the conditional probability

                val = conditional_key*p_key

                inter_res.append(val)


            normal_sum = 0
            for i in range(0,len(inter_res)):
                normal_sum = normal_sum + inter_res[i]

            final_res = []
            for j in range(0,len(inter_res)):
                final_res.append(inter_res[j]/normal_sum)


            player_choice = final_res.index(max(final_res)) # Estimate of the players next move

            util_res = []
            for i in range(0,len(final_res)):
                if i == 0:
                    utility = final_res[2] - final_res[1]
                    util_res.append(utility)
                elif i == 1:
                    utility = final_res[0] - final_res[2]
                    util_res.append(utility)
                elif i == 2:
                    utility = final_res[1] - final_res[0]
                    util_res.append(utility)

            our_move = util_res.index(max(util_res))

            print (str(our_move))
            terminal_output.append(r)
            terminal_output.append(our_move)
        prev_zk = zero_k # Updates to keep track of the previous counts for playing in case of k = 0








        # c = c + 1
        # ctr = ctr + 1




if __name__ == "__main__":
    main()
