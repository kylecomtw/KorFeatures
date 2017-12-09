import json
import pdb
from typing import List, Union

LexFeature = Union[str, List[str]]

class LexicalMatcher:
    def __init__(self):
        pass

    def match_features(self, inputs: List[str], feat_vec: List[LexFeature]):
        feat_map = {}
        if not isinstance(feat_vec, list):
            raise ValueError("feat_vec should be a vector of features")

        for feat_x in feat_vec:
            starti = 0
            n_feat_x = 0
            if not isinstance(feat_x, list):
                feat_x = [feat_x]
            n_occur = self.match_single_feature(inputs, feat_x)
            feat_map[tuple(feat_x)] = n_occur
        return feat_map
    
    import pdb
    def match_single_feature(self, inputs, feature: List[str]):
        starti = -1
        n_occur = 0
        # pdb.set_trace()
        while True:
            to_break = False
            
            for i, feat_x in enumerate(feature):            
                try:
                    starti = inputs.index(feat_x, starti+1)
                    if i == len(feature)-1:
                        n_occur += 1
                except:
                    to_break = True
                    break
            if to_break: break

        return n_occur
            
