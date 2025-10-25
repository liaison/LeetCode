class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        source_mapping = {}
        target_mapping = {}

        for index, letter in enumerate(s):
            source, target = s[index], t[index]

            if source in source_mapping:
                source = source_mapping[source]
                if source != target:
                    return False
                else:
                    # important step
                    continue
            else:
                source_mapping[source] = target

            if target in target_mapping:
                target = target_mapping[target]
                if source != target:
                    return False
            else:
                target_mapping[target] = source


        return True


    def isIsomorphic_alt(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        source_mapping = {}
        target_mapping = {}

        for index, letter in enumerate(s):
            source, target = s[index], t[index]

            if source not in source_mapping and target not in target_mapping:
                source_mapping[source] = target
                target_mapping[target] = source

            elif source_mapping.get(source) != target or target_mapping.get(target) != source:
                return False

        return True