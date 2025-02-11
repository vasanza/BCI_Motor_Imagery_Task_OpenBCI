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

# Tabla de registros
- ID Sujetos
- Nombres
- Apellidos
- Num. Repetición

# Protocolo
- Los sujetos serán recibidos por personal encargado de llevar a cabo el experimento que los atenderá amablemente. El personal evitará utilizar batas blancas o vestimenta médica, pero tampoco se utilizará colores llamativos que distraigan la atención de los sujetos durante el experimento.
- El personal encargado del experimento respetara las medidas de bioseguridad ante el riesgo del COVID-19, las medidas dispuestas por el ministerio de salud publica del gobierno del Ecuador incluyen: uso obligatorio de mascarillas, área de experimentación ventilada, superficies de contacto debidamente desinfectadas, así como limpieza de todos los utensilios utilizados antes y después de cada experimento. [https://www.salud.gob.ec/medidas-de-proteccion-basicas-contra-el-nuevo-coronavirus/]
- El ambiente donde se realizará el experimento no contará con dibujos infantiles que distraigan la atención de los sujetos de prueba.
- A cada sujeto se le hará firmar un consentimiento informado (ver anexo).
- A cada sujeto de prueba se le asignará un ID único que permitirá anonimizar sus datos demográficos y los datos registrados durante el experimento.
- Luego de que el sujeto de prueba firme el consentimiento informado, se le realizara una encuesta con los siguientes datos demográficos: https://forms.gle/965jAaHuoKRjLieP6
(Usar como ejemplo, este formulario es para los registros EEG)
- Los sujetos serán sentados en un sillón cómodo con sus extremidades superiores puestas sobre los apoya brazos del sillón y con un ángulo de codo de 145°. Por otro lado, las extremidades inferiores estarán suspendidas en el aire, apoyadas sobre un soporte de una altura de 25cm con un ángulo de 145° con respecto a sus muslos.
- Se colocará un monitor de pantalla de 17" a una distancia entre el plano objetivo y el acromion que correspondía al 80% de la longitud del brazo.
- ![image](https://user-images.githubusercontent.com/12642226/130649818-06206a15-ce56-4f0b-832f-40fbbf76a233.png) ![image](https://user-images.githubusercontent.com/12642226/130649824-c6c8ef17-119f-4d0e-aaf0-5eb415fac74a.png)
- A cada sujeto se colocará el sistema de registro de EEG que consta de un casco y 16 electrodos, distribuidos en el sistema internacional 10 - 20. No se usará gel conductor en cada electrodo ya que estos son de contacto seco.
- Antes de comenzar la adquisición de cada sesión, los investigadores impartirán instrucciones estandarizadas sobre la ejecución de las tareas a ejecutar a los participantes y se realizara una sesión corta de prueba.
- Se solicitará a cada participante que realice 10 sesiones (5 motoras y 5 imagenetico motoras) de 240 segundos de duración cada una (4min). En cada sesión los participantes realizarán 30 tareas que incluyen la ejecución de extremidades superiores e inferiores [78,79,110]. Cada sesión será identificada con un numero que va entre 1 – 10, permitiendo que el sujeto de prueba pueda continuar con sus sesiones en días posteriores si lo considera necesario.

# Tareas Motoras
- Durante las 5 sesiones de tareas motoras, el participante tendrá que mirar la pantalla y esperar hasta que aparezca la instrucción de tarea a ser ejecutada:
- Registrar un baseline con ojos abiertos (BEO) sin ninguna orden durante 4s.
- Registrar 30 tareas motoras (M) en forma aleatoria con tiempos aleatorios entre 4s de duración, intercaladas por 4s de descanso con ojos abiertos viendo monitor y relajando todos los músculos del cuerpo.
- Ejecución de movimiento, cerrar mano izquierda (LCH)
- Ejecución de movimiento, cerrar mano derecha (RCH)
- Ejecución de movimiento, flexión dorsal de pie izquierdo (LDF)
- Ejecución de movimiento, flexión plantar de pie izquierdo (LPF)
- Ejecución de movimiento, flexión dorsal de pie derecho (RDF)
- Ejecución de movimiento, flexión plantar de pie derecho (RPF)

# Tareas Imagenetico Motoras
- Durante las 5 sesiones posteriores de tareas imagenetico motoras, el participante tendrá que mirar la pantalla y esperar hasta que aparezca la instrucción de tarea a ser ejecutada:
- Registrar un baseline con ojos abiertos (BEO) sin ninguna orden durante 4s.
- Registrar 30 tareas imagenetico motoras (I) en forma aleatoria con tiempos aleatorios entre 4s de duración, intercaladas por 4s de descanso con ojos abiertos viendo monitor y relajando todos los músculos del cuerpo.
- Imaginar en primera persona, cerrar mano izquierda (LCH)
- Imaginar en primera persona, cerrar mano derecha (RCH)
- Imaginar en primera persona, flexión dorsal de pie izquierdo (LDF)
- Imaginar en primera persona, flexión plantar de pie izquierdo (LPF)
- Imaginar en primera persona, flexión dorsal de pie derecho (RDF)
- Imaginar en primera persona, flexión plantar de pie derecho (RPF)

- Durante una sesión el sujeto deberá realizar las 30 tareas arriba indicadas con las extremidades superiores o inferiores según sea el caso.
- Después de cada sesión, el sujeto podrá descansar por el período de tiempo que crea conveniente.
Cada sujeto de prueba vera en pantalla imágenes características que indicaran la tarea a realizar:
- ![image](https://user-images.githubusercontent.com/12642226/130650042-4e310018-5247-482b-a3c0-2120ced9f03c.png)

# Registrar un baseline con ojos abiertos (BEO) sin ningún estímulo visual.
![image](https://user-images.githubusercontent.com/12642226/130702170-755b4cc1-437c-4dff-9390-a5ab75a3b103.png)

# Descanso con ojos abiertos viendo monitor.
![image](https://user-images.githubusercontent.com/12642226/130702196-e6ce844b-d12b-4813-a5d7-19288e723d95.png)

# Cerrar mano izquierda (LCH).
![image](https://user-images.githubusercontent.com/12642226/130702223-174f5d2e-4a36-4c90-b830-c4c9b4e27243.png)

# Cerrar mano derecha (RCH).
![image](https://user-images.githubusercontent.com/12642226/130702235-f0c7031f-b339-48eb-b33b-32cef575e9f6.png)

# Flexión dorsal pie izquierdo (LDF).
![image](https://user-images.githubusercontent.com/12642226/130702250-d1bbdfd5-82a4-4bba-a366-fdcd6c226b26.png)

# Flexión plantar pie izquierdo (LPF).
![image](https://user-images.githubusercontent.com/12642226/130702268-8d3ba01b-c43d-4123-9490-fe3616c3ed13.png)

# Flexión dorsal pie derecho (RDF).
![image](https://user-images.githubusercontent.com/12642226/130702286-f2c5242a-3505-4e0a-b4ca-5cd8ea5d31dc.png)

# Flexión plantar pie derecho (RPF).
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
