my_list = [5, 2, 3, 4, 1, ]

def sort_part(the_list, low_idx, pivot_idx):
    pivot_val = the_list[pivot_idx]

    while pivot_idx != low_idx:
        low_val = the_list[low_idx]