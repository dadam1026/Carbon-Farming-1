def deforestation:
	metrics = [partial(accuracy_multi, thresh=0.2), FBetaMulti(beta=2, average='samples', thresh=0.2)]
	cbs = [MixUp]

	learn = cnn_learner(dls, resnet50, metrics=metrics, cbs=cbs).to_fp16()
	learn.lr_find()

	learn.fine_tune(6, base_lr=2e-2, freeze_epochs=4)

	learn.save('resnet50-128')

	learn.show_results()

	learn.export() # if we want .pkl file for proper end to end deployment (file will be saved as export.pkl)

	#inference = learn.load('resnet50-128')

	

def prediction(filename='submission.csv', tta=False):
    tst_dl = learn.dls.test_dl(testing_path)
    if tta:
        predictions = learn.tta(dl = tst_dl)
    else:
        predictions = learn.get_preds(dl = tst_dl)
    predlist = [' '.join(learn.dls.vocab[i]) for i in (predictions[0] > 0.2)]

    df = submission_df
    df['tags'] = predlist

    df.to_csv(filename, index=False)
    return df

if __name__ == "__main__":
	
	additional_test_path = Path('test-jpg-additional/test-jpg-additional')

	test_path = Path('planet/planet/test-jpg')

	submission_df = pd.read_csv(path/'sample_submission.csv')

	testing_path = (submission_df['image_name'] + '.jpg').apply(lambda x: test_path/x if x.startswith('test') else additional_test_path/x)
    deforestation()  # pylint: disable=no-value-for-parameter
    prediction()