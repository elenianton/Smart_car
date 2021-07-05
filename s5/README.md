# PROJECT DESCRIPTION

This directory contains a recipe (based on mini librispeech) to build a speech recognition system (ASR) for a Greek car voice assistant named "Smart Car". Our system is meant to facilitate driver's experience. Significantly, it is developed to recognize four different kinds of voice commands: 

1. navigation commands
2. communication commands
3. entertainment commands
4. commands related to certain car functions

# CUSTOMIZATION PROCESS

Our ASR system was trained on a subset of the “Logotypografia” Greek corpus, consisting of 8192 audio files of high-quality utterances recorded by a close-talk microphone. The total duration of the data is 16 hours approximately. 

A part (20%) of the recorded data was used as development set.

For testing purposes, we have automatically produced 200 task-specific phrases, based on a grammar we have developed, using HTK toolkit. Then, we selected 150 among them to be uttered by 6 speakers, and to be used as test data.

To create our task-specific recipe we have adapted mini librispeech scripts and we have developed new ones in Python. Our dictionary was produced out of a large Greek phonetic transcriptions dictionary (Greek400k.dictionary). For unseen words we have used phonemizer tool, adjusting the output transcriptions to match the transcription format of the initial dictionary. Our data directories have been processed to match Kaldi's required format.

# HOW TO RUN SMART CAR RECIPE

* First run "run.sh" to train our customized model and test it on development data.
* Then, run "run_test.sh" to test our model on task-specific data.

# RESULTS

## *Development set*
	
	wer_9_0.5  > %WER 43.15 [ 14151 / 32796, 1774 ins, 3816 del, 8561 sub ]
	wer_14_0.0 > %WER 41.83 [ 13718 / 32796, 1431 ins, 4053 del, 8234 sub ]
	wer_17_0.5 > %WER 41.45 [ 13593 / 32796, 1129 ins, 4376 del, 8088 sub ]
	wer_11_0.5 > %WER 42.31 [ 13877 / 32796, 1537 ins, 3985 del, 8355 sub ]
	wer_14_1.0 > %WER 41.56 [ 13631 / 32796, 1165 ins, 4346 del, 8120 sub ]
	wer_7_0.5  > %WER 44.66 [ 14648 / 32796, 2142 ins, 3649 del, 8857 sub ]
	wer_12_0.5 > %WER 41.99 [ 13771 / 32796, 1440 ins, 4053 del, 8278 sub ]
	wer_7_1.0  > %WER 44.28 [ 14522 / 32796, 1993 ins, 3717 del, 8812 sub ]
	wer_17_1.0 > %WER 41.45 [ 13593 / 32796, 1012 ins, 4528 del, 8053 sub ]
	wer_8_1.0  > %WER 43.46 [ 14253 / 32796, 1793 ins, 3842 del, 8618 sub ]
	wer_10_0.0 > %WER 42.96 [ 14089 / 32796, 1814 ins, 3785 del, 8490 sub ]
	wer_15_1.0 > %WER 41.41 [ 13581 / 32796, 1103 ins, 4401 del, 8077 sub ]
	wer_10_1.0 > %WER 42.42 [ 13913 / 32796, 1495 ins, 4014 del, 8404 sub ]
	wer_13_0.0 > %WER 41.93 [ 13751 / 32796, 1505 ins, 3992 del, 8254 sub ]
	wer_17_0.0 > %WER 41.50 [ 13609 / 32796, 1269 ins, 4225 del, 8115 sub ]
	wer_15_0.5 > %WER 41.47 [ 13600 / 32796, 1217 ins, 4270 del, 8113 sub ]
	wer_15_0.0 > %WER 41.67 [ 13665 / 32796, 1381 ins, 4121 del, 8163 sub ]
	wer_16_0.5 > %WER 41.44 [ 13591 / 32796, 1167 ins, 4330 del, 8094 sub ]
	wer_8_0.0  > %WER 44.16 [ 14483 / 32796, 2122 ins, 3638 del, 8723 sub ]
	wer_13_0.5 > %WER 41.74 [ 13689 / 32796, 1352 ins, 4119 del, 8218 sub ]
	wer_16_1.0 > %WER 41.40 [ 13576 / 32796, 1052 ins, 4471 del, 8053 sub ]
	wer_9_1.0  > %WER 42.87 [ 14059 / 32796, 1630 ins, 3911 del, 8518 sub ]
	wer_13_1.0 > %WER 41.58 [ 13637 / 32796, 1210 ins, 4269 del, 8158 sub ]
	wer_16_0.0 > %WER 41.59 [ 13641 / 32796, 1326 ins, 4166 del, 8149 sub ]
	wer_9_0.0  > %WER 43.46 [ 14253 / 32796, 1934 ins, 3714 del, 8605 sub ]
	wer_12_0.0 > %WER 42.27 [ 13864 / 32796, 1608 ins, 3924 del, 8332 sub ]
	wer_11_1.0 > %WER 42.06 [ 13793 / 32796, 1383 ins, 4104 del, 8306 sub ]
	wer_7_0.0  > %WER 45.05 [ 14773 / 32796, 2295 ins, 3578 del, 8900 sub ]
	wer_14_0.5 > %WER 41.61 [ 13648 / 32796, 1272 ins, 4209 del, 8167 sub ]
	wer_10_0.5 > %WER 42.62 [ 13977 / 32796, 1642 ins, 3896 del, 8439 sub ]
	wer_11_0.0 > %WER 42.53 [ 13949 / 32796, 1697 ins, 3853 del, 8399 sub ]
	wer_8_0.5  > %WER 43.75 [ 14348 / 32796, 1955 ins, 3722 del, 8671 sub ]
	wer_12_1.0 > %WER 41.81 [ 13713 / 32796, 1294 ins, 4173 del, 8246 sub ]

## *Test set*
	
	 %WER 17.07 [ 120 / 703, 12 ins, 91 del, 17 sub ] [PARTIAL]
	 	
	
### Most Common Errors:
    
#### SENTENCE RECOGNITION PERFORMANCE

	sentences                               147
	with errors                  100.0%   ( 147)

	with substitions              97.3%   ( 143)
   	with deletions                19.7%   (  29)
   	with insertions               4.8%    (   7)


#### WORD RECOGNITION PERFORMANCE

	Percent Total Error          101.0%   ( 710)

	Percent Correct                0.0%   (   0)

	Percent Substitution          87.8%   ( 617)
	Percent Deletions             12.2%   (  86)
	Percent Insertions             1.0%   (   7)
	Percent Word Accuracy         -1.0%


	Ref. words                            ( 703)
	Hyp. words                            ( 624)
	Aligned words                         ( 710)

# **SUGGESTIONS FOR WER IMPROVEMENT**
	
* Add more alternative term pronunciations in the lexicon.
* Check and improve transcriptions.
* Train the model with task-specific data.
* Improve audio data quality.

# **SYNTHESIS PROJECT DESCRIPTION**
Our "Smart Car" voice assistant can be enriched with a speech synthesis system to improve user's experience. As it is meant to be used during driving, it would be useful for the driver to hear the system's output instead of reading it on screen.

## **PHRASES**
We have extracted 10 phrases (5 using merlin's demo voice and 5 using merlin's full voice) for our system. These phrases are the system's responses to the user's commands.

### DEMO VOICE
* Τhe nearest gas station is 1 km away.
* Now playing MAD Radio FM.
* Front left window is open. Please remember to close it before you leave the car.
* Front right door is still open. 
* Best route calculation.

### FULL VOICE 
* Where would you like to go?
* Air-conditioning deactivated
* Air-conditioning activated
* Front right window closed
* Radio is off

# SYNTHESIS EVALUATION RESULTS - MOS CALCULATION
## DEMO VOICE
* Intelligibility  
    Phrase 1         Phrase 2        Phrase 3          Phrase 4          Phrase 5
	member 1 >  2    member 1 > 2    member 1 > 1      member 1 > 1      member 1 > 2
	member 2 >  2    member 2 > 2    member 2 > 1      member 2 > 1      member 2 > 2
    member 3 >  2    member 3 > 2    member 3 > 2      member 3 > 2      member 3 > 2
	MOS      >  2    MOS      > 2    MOS      > 1.33   MOS      > 1.33   MOS      > 2
  
   
* Naturalness    
    Phrase 1         Phrase 2        Phrase 3          Phrase 4           Phrase 5
	member 1 >  1    member 1 > 1    member 1 > 1      member 1 > 1       member 1 > 2
	member 2 >  1    member 2 > 1    member 2 > 1      member 2 > 1       member 2 > 2
    member 3 >  1    member 3 > 1    member 3 > 1      member 3 > 1       member 3 > 2
	MOS      >  1    MOS      > 1    MOS      > 1      MOS      > 1       MOS      > 2

## FULL VOICE
* Intelligibility  
    Phrase 6         Phrase 7        Phrase 8          Phrase 9           Phrase 10
	member 1 >  5    member 1 > 5    member 1 > 5      member 1 > 3       member 1 > 5
	member 2 >  5    member 2 > 5    member 2 > 5      member 2 > 4       member 2 > 5
    member 3 >  5    member 3 > 5    member 3 > 5      member 3 > 3       member 3 > 5
	MOS      >  5    MOS      > 5    MOS      > 5      MOS      > 3.33    MOS      > 5
  
   
* Naturalness    
  Phrase 6           Phrase 7        Phrase 8          Phrase 9           Phrase 10
	member 1 >  4    member 1 > 4    member 1 > 4      member 1 > 3       member 1 > 4
	member 2 >  4    member 2 > 4    member 2 > 4      member 2 > 3       member 2 > 4
    member 3 >  4    member 3 > 4    member 3 > 4      member 3 > 3       member 3 > 4
	MOS      >  4    MOS      > 4    MOS      > 4      MOS      > 3       MOS      > 4

# **SUGGESTIONS FOR MOS IMPROVEMENT**
To improve MOS scores on intellibility, the system could be trained on speech with a natural flow without breaks in the synthesis signal.

To improve MOS scores on naturaleness, the system could be trained on spontaneous/natural speech, instead of read speech. 
