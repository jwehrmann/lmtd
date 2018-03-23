from __future__ import print_function
import numpy as np
import database as db
from file_utils import load_json
from file_utils import load_pickle 


class LMTD:

	def __init__(self):
		'''
			features_file: path the features dictionary
		'''		
		self.__fetch_splits__()

	def load_precomp_features(self, features_file='../features/lmtd9_resnet152.pickle'):
		self.feature_dict = load_pickle(features_file)	

	def get_split_ids(self, split='train'):		
		self.ids, self.labels, self.genres = db.get_split(split)
		return self.ids, self.labels, self.genres

	def get_split(self, split='train'):

		print('loading {} ... '.format(split))		

		self.ids, self.labels, self.genres = self.get_split_ids(split)
		self.features, self.lenghts = __align_split_features__(self.ids, self.feature_dict)

		return self.features, self.lenghts, self.labels, self.ids

	def get_data_by_trailer_ids(self, trailer_ids):
		return db.get_data_by_trailer_ids(trailer_ids)

	def binary_label_to_genre(self, binary_labels):
		
		binary_labels = np.asarray(binary_labels)
		get_gen_fn = lambda x: sorted([self.genres[x == 1]])
		
		if len(binary_labels.shape) == 2:
			genres = [list(get_gen_fn(x)) for x in binary_labels]
		else:
			genres = get_gen_fn(binary_labels)		

		return genres

	def __fetch_splits__(self, ):
		self.train_ids, self.train_labels, self.genres = db.get_split('train')
		self.valid_ids, self.valid_labels, _ = db.get_split('valid')
		self.test_ids,  self.test_labels,  _ = db.get_split('test')


def __pad_sequence__(seq, maxlen):

	left = 0 if maxlen < len(seq) else (maxlen - len(seq))	
	left_pad = np.zeros((left, len(seq[-1])))

	pad_feat = np.concatenate([seq, left_pad], 0)[:maxlen]
	return pad_feat


def __align_split_features__(ids, feature_dict, maxlen=240):
		feats = []
		lens = []

		for id in ids:
			
			feat = np.asarray(feature_dict[id])
			
			if len(feat.shape) != 2:
				print(id)
				continue

			_pad_feat = __pad_sequence__(feat, maxlen=maxlen)			
			
			feats.append(_pad_feat)
			lens.append(len(feature_dict[id]))

		return np.asarray(feats), np.asarray(lens)

