# Digital Signal Processing
## Project Title: Sea Turtle photo ID

#### Pigi Lozou
#### 14/10/2019

### Loggerhead sea turtle (Caretta caretta)

The Caretta turtle, Caretta caretta (Linnaeus, 1758) is a species of sea turtle found in the Atlantic, Pacific and Indian Oceans, as well as the Mediterranean Sea. These turtles have, on average, a final shell length of 90 cm. An adult turtle weighs about 135 kg. The skin color ranges from yellow to brown and the eel is usually reddish-brown. Until the turtle reaches adulthood, racial differences are not visible. The main sex characteristic is that adult males have longer tails and claws than females.
Greece and especially the coasts of Zakynthos and Kyparissia are the most popular nesting area along the Mediterranean, with more than 3,000 nests per year. The Caretta turtle spends most of its life in the sea. Females go ashore for a while to lay eggs. It has a low reproductive rate: females lay an average of four clutches of eggs and then remain inactive and do not spawn again for two to three years. It reaches sexual maturity between the ages of 17–33 and has a lifespan of 47–67 years.[1]
Sea turtles are considered an endangered species and are protected by the International Union for Conservation of Nature. Abandoned and in-use fishing gear is responsible for many turtle deaths. Special devices have been placed in the nets in an effort to reduce mortality, providing an escape route for the turtles. The loss of suitable nesting beaches due to tourism and commercial interest have also affected the turtle population. Also, their path in life begins with many enemies such as crabs, seagulls, fish, rodents but also dangers such as human activities on the beaches and in the sea. Only 1 in 1000 baby turtles will survive to adulthood! Efforts to restore their numbers require more general cooperation, given that turtles roam vast areas of the ocean and nesting beaches are scattered across different countries. In this context, in 1983 the Association for the Protection of the Sea Turtle "Archelon" was established, a non-profit association with the object of the study, protection and care of Caretta turtles, as well as the management of the ecosystems in the most important Greek nesting beaches . [2]

### Facial recognition 

The Association for the Protection of the Sea Turtle 'ARCHELON' takes measures to monitor and protect the sea turtle in Greece. In particular, it deals with the methods of locating and recording nests and their incubation and hatching data. The project also includes recording the protection measures taken in the nests of the Caretta caretta species to protect against natural and anthropogenic pressures and threats. We could mention that the continuous monitoring of the scientific methodology for the preservation of the sea turtle population is necessary. [3]
The purpose of this research work is the automatic identification of individual turtles in order to better and more efficiently record data for the monitoring and protection of this endangered species.
Face identification using photographs (Photo-ID) is a scientific method for "tagging" animals. Photo-ID is a cost-effective yet non-invasive method that can easily be used to track sea turtles without any intervention on them.
Different turtles can be identified by the different patterns on their faces which are unique and make up their imprint. (Picture 1)
Tools: PyTorch is an open source machine learning library based on the Torch library. It is used for computer vision applications as well as natural language processing.
Database
For the data, part of the database (9 individuals) of Kostantinos Papafitsouros [5] who has a wide sorted collection (over 1000 individuals) of loggerhead turtle photos was provided. From 400 to 1000 photos are available for each person.

### Building a neural network for caret recognition with random image selection

First, the data was organized into addresses.
  data/train/tXXX for training
  data/val/tXXX for evaluation
Where tXXX is the folder with the photos of each turtle.
Images for evaluation were selected by randomly selecting one-tenth of the total images for each turtle.

The neural network was then trained in two ways
Initialization of the parameters with a pre-trained network (Finetuning): Instead of a random initialization, the network is initialized with a pre-trained network like that of imagenet which has more than 1000 objects.
Convolutional neural network as a fixed feature extractor: Here a pre-trained network is used unchanged except for the last fully connected layer. This last layer is initialized with one with random weights and is the only one that is trained.
The execution of this step was done with the python file ``` makeNdatasets.py```, ```turtles_train_ft.py``` and ```turtles_train_conv.py``` after first making the train and val folders. The results are summarized in Table:


Finetuning convnet accuracy | Fixed feature extractor accuracy
----|----
0.95452 | 0.761686

### Building a neural network for caret recognition with random shots

First, the data was organized into addresses.
  data/train/tXXX/sk for training
  data/val/tXXX/sk for evaluation
Where tXXX is the folder with the photos of each turtle and sk is the k-th different shot.
By shooting we mean the set of photos that were taken in the same location at the same time. The selection of shots for evaluation was done by randomly selecting one shot for each turtle.

Then the neural network was trained in both ways as before by choosing 5 different combinations of train and val.
Initialization of parameters with pre-trained network (Finetuning).
Convolutional neural network as a fixed feature extractor.
The execution of this step was done with the python file ```makeNdatasets.py``` where first the train and val folders are made and then the training is done as before by calling the files ```turtles_train_ft.py``` and ```turtles_train_conv.py```. The results are summarized in Table:

Random shots dataset | Finetuning convnet accuracy |Fixed feature extractor accuracy
----|----|----
1 | 0.812500 | 0.681686
2 | 0.847101 | 0.628261
3 | 0.711221 | 0.620462
4 | 0.714286 | 0.565392
5 | 0.667669 | 0.365414


### Observations-Conclusions-Extensions

We notice that when the training is done with a random selection of images then they have a very good performance in the evaluation (95%!). This happens because the images taken have a similar background, so the network recognizes the turtle by extracting information from the background as well. But this is not legitimate. This is how download separation was tested. We see that by separating the shots the accuracy drops. This is probably due to the fact that in each image there is a large amount of unnecessary information (background, environment, even the shell can be misleading). As described in the introduction, the separation of turtles is done by the shapes of the face. In the context of this work, however, the entire images were used as they were in the database. So this study could be extended and improved using only the face for recognition.


### References-Bibliography
[1] https://marinebio.org/species/loggerhead-sea-turtles/caretta-caretta/

[2] https://www.wwf.gr/endangered-species/caretta 

[3] http://ekpaa.ypeka.gr/index.php/draseis/ektheseis/item/124-methods-of-sea-turtle-monitoring-protection-in-greece

[4]https://pytorch.org/ 

[5] http://kostaspapafitsoros.weebly.com/
