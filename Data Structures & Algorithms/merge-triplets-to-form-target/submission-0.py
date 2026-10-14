class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # one simpel fact that all pairs who have any of theri tripelt element greter than target truiplet elements ruin the anaswer so tehyar e not consdiered valid marge candidates
        # out of the remianig merge candidates we simply look if we can find each of the candaite triplet
        # if yes then deffinely as we are super flexible in our mergingw e ill reach teh overall target
        # teh greed criteria here is that lcoally if im a atrget of teh triplet im just concenrned about elements gretaer than myslef are not allowed rest is fine

        # 3 loops for each of the 3 target
        for i in range(0,3):
            to_find = target[i]
            target_found = False
            for pair in triplets:
                if pair[0] <= target[0] and pair[1] <= target[1] and pair[2] <= target[2]:
                    # so these are our valid candiadtes
                    # print(pair[i],target_found)
                    if pair[i] == to_find:
                        target_found = True
                        continue
            if not target_found:
                return False
        return True
                