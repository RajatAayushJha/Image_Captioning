def preprocessing():
	image_captions = open("Flickr8k.lemma.token.txt").read().split('\n')
	caption = {}
	
	for i in range(len(image_captions)-1):
		id_capt = image_captions[i].split("\t")
		#print(id_capt[0])
		t=id_capt[0]
		t=t[:-2]
		#print(t)
		id_capt[0] = t 	# to rip off the #0,#1,#2,#3,#4 from the tokens file
		if id_capt[0] in caption:
			caption[id_capt[0]].append(id_capt[1])
		else:
			caption[id_capt[0]]=[id_capt[1]]
	train_imgs_id = open("Flickr_8k.trainImages.txt").read().split('\n')[:-1]

	
	train_imgs_captions = open("trainimgs.txt",'w')
	for img_id in train_imgs_id:
		#print(img_id)
		for captions in caption[img_id]:
			desc = "<start> "+captions+" <end>"
			train_imgs_captions.write(img_id+"\t"+desc+"\n")
			train_imgs_captions.flush()
	train_imgs_captions.close()

	test_imgs_id = open("Flickr_8k.testImages.txt").read().split('\n')[:-1]

	test_imgs_captions = open("testimgs.txt",'w')
	for img_id in test_imgs_id:
		for captions in caption[img_id]:
			desc = "<start> "+captions+" <end>"
			test_imgs_captions.write(img_id+"\t"+desc+"\n")
			test_imgs_captions.flush()
	test_imgs_captions.close()

 

if __name__=="__main__":
	preprocessing()