class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company_set = set()
        for company_list in favoriteCompanies:
            company_set.update(company_list)

        company_dict = dict()
        for index, company in enumerate(company_set):
            company_dict[company] = 1 << index

        def get_bitmap(companies):
            bitmap = 0
            for company in companies:
                bitmap |= company_dict[company]
            return bitmap

        bitmap_dict = {}
        # more space to exchange for computing time
        for a_index, a_list in enumerate(favoriteCompanies):
            bitmap_dict[a_index] = get_bitmap(a_list)

        ret = []
        for a_index, a_list in enumerate(favoriteCompanies):
            is_subset = False
            for b_index, b_list in enumerate(favoriteCompanies):
                if a_index != b_index:
                    a_bitmap = bitmap_dict[a_index]
                    b_bitmap = bitmap_dict[b_index]
                    if (a_bitmap & b_bitmap) == a_bitmap:
                        # a_list is a sublist of b_list
                        is_subset = True
                        break
            if not is_subset:
                ret.append(a_index)

        return ret


