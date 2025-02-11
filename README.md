# BCI_Motor_Imagery_Task_OpenBCI
Motor and Imagery task using EEG Signals recolected by OpenBCI

# [MILimbEEG](https://data.mendeley.com/datasets/w9xfz56txv/2)
Biomedical Electroencephalography (EEG) signals are the result of measuring the electric potential difference generated on the scalp surface by neural activity corresponding to each brain area. Accurate and automatic detection of neural activity from the upper and lower limbs using EEG may be helpful in rehabilitating people suffering from mobility limitations or disabilities. This article presents a dataset containing 7440 CSV files from 60 test subjects during motor and motor imagery tasks. The motor and motor imagery tasks performed by the test subjects were: Closing Left Hand (CLH), Closing Right Hand (CRH), Dorsal flexion of Left Foot (DLF), Plantar flexion of Left Foot (PLF), Dorsal flexion of Right Foot (DRF), Plantar flexion of Right Foot (PRF) and Resting in between tasks (Rest). The volunteers were recruited from research colleagues at ESPOL and patients at the Luis Vernaza Hospital in Guayaquil, Ecuador. Each CSV file has 501 rows, of which the first one lists the electrodes from 0 to 15, and the remaining 500 rows correspond to 500 data recorded during the task is performed due to sample rate. In addition, each file has 17 columns, of which the first one indicates the sampling number and the remaining 16 columns represent 16 surface EEG electrodes. As a data recording equipment, the OpenBCI is used in a monopolar setup with a sampling rate of 125 Hz. This work includes statistical measures about the demographic information of all recruited test subjects. Finally, we outline the experimental methodology used to record EEG signals during upper and lower limb task execution. This dataset is called MILimbEEG and contains microvolt (µV) EEG signals acquired during motor and motor imagery tasks. The collected data may facilitate the evaluation of EEG signal detection and classification models dedicated to task recognition.

Database for Upper and Lower Limb Task Based on EEG Signals During the Execution of Motor and Motorimagery Tasks
- **Journal**: https://www.sciencedirect.com/science/article/pii/S2352340923006406?via%3Dihub
- Main Code: https://github.com/Human-Machine-Interface/OpenBCI_Data_Acquisition
- Data Mendeley: https://data.mendeley.com/datasets/x8psbz3f6x/2
- More Matlab Examples: https://github.com/Human-Machine-Interface
- Hardware: FM=16 chanels , Cyton + Dasy , Campling Rate = 125 Hz
- Subjects: 60

# Equipment
We use the OpenBCI Cyton + Daisy (www.openbci.com) [1] Biosensing Board for EEG signal recording. The equipment has an active bandpass filter in the 5 to 50 Hz range, additionally, a notch filter at 60 Hz [1]. This non-invasive device operates within a sampling frequency of 125 Hz and has 16 dry electrodes with two ground references, distributed in the international 10–20 system. All 16 EEG electrodes were recorded in monopolar configuration, in which the potential of each electrode is compared with a neutral electrode located in both lobes of the ears [2]. To guarantee the replicability of the EEG signal recording, the international 10/10 system standardized by the AES was used [10]. The distribution of the 16 electrodes is shown in the figure:

![image](https://github.com/user-attachments/assets/0585a66f-c9a4-4255-9215-ce7315257354)

The connections of the electrodes to the Cyton and Dazzy PCBs are as follows:
- [Cyton board](https://docs.openbci.com/Cyton/CytonLanding/)
  - Electrode 1: CH1 (FC5 in 10-10 system EEG)
  - Electrode 2: CH2 (F3 in 10-10 system EEG)
  - Electrode 3: CH3 (FZ in 10-10 system EEG)
  - Electrode 4: CH4 (F4 in 10-10 system EEG)
  - Electrode 5: CH5 (FC5 in 10-10 system EEG)
  - Electrode 6: CH6 (FC1 in 10-10 system EEG)
  - Electrode 7: CH7 (FC2 in 10-10 system EEG)
  - Electrode 8: CH8 (CZ in 10-10 system EEG)
- [Dazzy board](https://docs.openbci.com/GettingStarted/Boards/DaisyGS/)
  - Electrode 9: CH1 (T3 in 10-10 system EEG)
  - Electrode 10: CH2 (CP5 in 10-10 system EEG)
  - Electrode 11: CH3 (C3 in 10-10 system EEG)
  - Electrode 12: CH4 (CP1 in 10-10 system EEG)
  - Electrode 13: CH5 (CP2 in 10-10 system EEG)
  - Electrode 14: CH6 (C4 in 10-10 system EEG)
  - Electrode 15: CH7 (CP6 in 10-10 system EEG)
  - Electrode 16: CH8 (T4 in 10-10 system EEG)
This is summarized in the following image:
![ultracoretex_mark4_nodelocation](https://github.com/user-attachments/assets/a4064d1b-d4b8-4ed7-acdc-b184a2b40fbb)

# Experimental Methodology
- At least 20 young adult subjects (without gender discrimination) aged between 20 and 35 years will be recruited to form the test group. Amputee subjects.
- Members of the pathological group should preferably be right-handed, assessed using the Edinburgh Handedness Inventory. They must not have a history of brain surgery or other pathologies related to the central nervous system, such as epilepsy, mental disabilities, etc. Additionally, they must have the ability to understand and follow instructions.
- Exclusion criteria will include: severe cognitive impairment, sensory deficits (such as auditory or perceptual impairments), and severe spasticity that prevents the execution of motor activities (Modified Ashworth Scale >3). The use of medications that affect task performance will also be an exclusion criterion.
- Participants will be recruited from the Escuela Superior Politécnica del Litoral (ESPOL) in the city of Guayaquil.
- Each test subject will be informed about the purpose of the experiment and will sign an informed consent form before participating in the study.

# Records Table
- ID Sujetos
- Nombres
- Apellidos
- Num. Repetición

# Protocol
- Subjects will be welcomed by the personnel conducting the experiment, who will attend to them courteously. The staff will avoid wearing white lab coats or medical attire, but they will also refrain from using bright colors that could distract the subjects during the experiment.
- The experiment staff will adhere to biosecurity measures to mitigate the risk of COVID-19. The measures, as mandated by the Ministry of Public Health of Ecuador, include: mandatory use of face masks, a well-ventilated experimental area, properly disinfected contact surfaces, and cleaning of all equipment before and after each experiment. [https://www.salud.gob.ec/medidas-de-proteccion-basicas-contra-el-nuevo-coronavirus/]
- The environment where the experiment will be conducted will not contain childish drawings or elements that could distract the subjects.
- Each subject will be required to sign an informed consent form (see annex).
- Every test subject will be assigned a unique ID to anonymize their demographic data and all recorded information during the experiment.
- Once the informed consent form is signed, each subject will complete a survey collecting demographic data: [https://forms.gle/965jAaHuoKRjLieP6] (This form serves as an example and is intended for EEG recordings.)
- Subjects will be seated in a comfortable chair, with their upper limbs resting on the armrests, ensuring a 145° elbow angle. Meanwhile, their lower limbs will remain suspended in the air, supported by a 25 cm high footrest, maintaining a 145° angle with their thighs.
- A 17-inch screen monitor will be placed at a distance corresponding to 80% of the arm length between the target plane and the acromion.
- ![image](https://user-images.githubusercontent.com/12642226/130649818-06206a15-ce56-4f0b-832f-40fbbf76a233.png) ![image](https://user-images.githubusercontent.com/12642226/130649824-c6c8ef17-119f-4d0e-aaf0-5eb415fac74a.png)
- Each subject will be fitted with the EEG recording system, which consists of a helmet and 16 electrodes, distributed according to the International 10-20 system. Conductive gel will not be used on the electrodes, as they are dry-contact electrodes.
- Before starting each session's data acquisition, the researchers will provide standardized instructions regarding the execution of the tasks to be performed by the participants. A short trial session will also be conducted.
- Each participant will be asked to complete 10 sessions (5 motor and 5 motor imagery) lasting 240 seconds (4 minutes) each. During each session, participants will perform 30 tasks, which include the execution of upper and lower limb movements [78,79,110]. Each session will be identified with a number between 1 and 10, allowing the test subject to continue their sessions on later days if necessary.

# Motor Tasks
- During the 5 sessions of motor tasks, the participant will have to look at the screen and wait for the task instruction to appear:
- Record a baseline with eyes open (BEO) without any command for 4 seconds.
- Record 30 motor tasks (M) in a random order, with random durations of 4 seconds, interspersed with 4-second rest periods, during which the participant will keep their eyes open, looking at the monitor, and relaxing all body muscles.
- Movement execution tasks:
  - Close left hand (LCH)
  - Close right hand (RCH)
  - Dorsiflexion of the left foot (LDF)
  - Plantar flexion of the left foot (LPF)
  - Dorsiflexion of the right foot (RDF)
  - Plantar flexion of the right foot (RPF)

# Motor Imagery Tasks
- During the following 5 sessions of motor imagery tasks, the participant will have to look at the screen and wait for the task instruction to appear:
- Record a baseline with eyes open (BEO) without any command for 4 seconds.
- Record 30 motor imagery tasks (I) in a random order, with random durations of 4 seconds, interspersed with 4-second rest periods, during which the participant will keep their eyes open, looking at the monitor, and relaxing all body muscles.
- First-person motor imagery tasks:
  - Imagine closing left hand (LCH)
  - Imagine closing right hand (RCH)
  - Imagine dorsiflexion of the left foot (LDF)
  - Imagine plantar flexion of the left foot (LPF)
  - Imagine dorsiflexion of the right foot (RDF)
  - Imagine plantar flexion of the right foot (RPF)

- During a session, the subject must perform the 30 tasks listed above using either the upper or lower limbs, as applicable.
- After each session, the subject may rest for as long as they deem necessary.
- Each test subject will see specific images on the screen indicating the task to be performed.
- ![image](https://user-images.githubusercontent.com/12642226/130650042-4e310018-5247-482b-a3c0-2120ced9f03c.png)

# Record a baseline with eyes open (BEO) without any visual stimulus.
![image](https://user-images.githubusercontent.com/12642226/130702170-755b4cc1-437c-4dff-9390-a5ab75a3b103.png)

# Rest with eyes open, looking at the monitor.
![image](https://user-images.githubusercontent.com/12642226/130702196-e6ce844b-d12b-4813-a5d7-19288e723d95.png)

# Close left hand (LCH).
![image](https://user-images.githubusercontent.com/12642226/130702223-174f5d2e-4a36-4c90-b830-c4c9b4e27243.png)

# Close right hand (RCH).
![image](https://user-images.githubusercontent.com/12642226/130702235-f0c7031f-b339-48eb-b33b-32cef575e9f6.png)

# Dorsiflexion of the left foot (LDF).
![image](https://user-images.githubusercontent.com/12642226/130702250-d1bbdfd5-82a4-4bba-a366-fdcd6c226b26.png)

# Plantar flexion of the left foot (LPF).
![image](https://user-images.githubusercontent.com/12642226/130702268-8d3ba01b-c43d-4123-9490-fe3616c3ed13.png)

# Dorsiflexion of the right foot (RDF).
![image](https://user-images.githubusercontent.com/12642226/130702286-f2c5242a-3505-4e0a-b4ca-5cd8ea5d31dc.png)

# Plantar flexion of the right foot (RPF).
![image](https://user-images.githubusercontent.com/12642226/130702296-11429b29-fdb8-4877-9104-04d8b4bb7661.png)

# Keynote
## Clone
- git status
- git clone https://github.com/vasanza/BCI_Motor_Imagery_Task_OpenBCI.git

## Switched to Branch
- git branch -a
- git checkout NameBranch

## New Branch
- git checkout -b NameBranch

## Push
- git pull origin NameBranch
- git status
- git add .
- git status
- git commit -m "message"
- git push origin NameBrach
