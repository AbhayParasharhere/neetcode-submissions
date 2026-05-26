class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        shorter = nums1 if len(nums1) <= len(nums2) else nums2
        longer = nums1 if len(nums1) > len(nums2) else nums2
        total = len(nums1) + len(nums2)
        goal_rank = total // 2
        even = total % 2 == 0

        def get_rank(candidate_val, candidate_pos, other_arr):
            # Count elements in other_arr that are <= candidate_val
            lo, hi = 0, len(other_arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if other_arr[mid] > candidate_val:
                    hi = mid
                else:
                    lo = mid + 1
            return candidate_pos + lo, lo

        def get_rank_strict(candidate_val, candidate_pos, other_arr):
            # Count elements in other_arr that are STRICTLY < candidate_val
            lo, hi = 0, len(other_arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if other_arr[mid] >= candidate_val:
                    hi = mid
                else:
                    lo = mid + 1
            return candidate_pos + lo, lo

        def find_median_in(primary, secondary):
            """BS on primary array to find the element at goal_rank."""
            l, r = 0, len(primary)
            while l < r:
                m = (l + r) // 2
                rank, _ = get_rank(primary[m], m, secondary)
                # rank = upper bound position (last slot this value could fill)
                # strict_rank = lower bound position (first slot this value could fill)
                strict_rank, _ = get_rank_strict(primary[m], m, secondary)
                # If goal_rank falls in [strict_rank, rank), this element IS the median
                # If rank <= goal_rank, candidate too small
                # If strict_rank > goal_rank, candidate too big
                if rank < goal_rank:
                    l = m + 1
                elif strict_rank > goal_rank:
                    r = m
                else:
                    # goal_rank falls within [strict_rank, rank] — found it
                    med = primary[m]
                    if even:
                        if goal_rank - 1 < strict_rank:
                            # The element at goal_rank-1 is NOT this same value
                            cand1 = primary[m - 1] if m > 0 else float('-inf')
                            # Need position in secondary just before strict_lo
                            _, strict_lo = get_rank_strict(primary[m], m, secondary)
                            cand2 = secondary[strict_lo - 1] if strict_lo > 0 else float('-inf')
                            med0 = max(cand1, cand2)
                        else:
                            # goal_rank-1 also falls in the range — same value
                            med0 = med
                        return (med + med0) / 2.0
                    return float(med)
            return None  # Not found in this array

        # Try shorter first, then longer
        result = find_median_in(shorter, longer)
        if result is not None:
            return result
        return find_median_in(longer, shorter)