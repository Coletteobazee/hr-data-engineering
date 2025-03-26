## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Answer:
The missing values and "NO DATA" values in the data/phase0.txt would occur due to several factors including:
1. Sensor issues, in that the heart rate moniteor may not pick up readings properly if it loses contact or has hardware problems like low battery or software glitches, also, sudden movements,sweating or changes in posture can affect the sensor reading appropriately.

2. The device may malfunction due to signal loss or interference

3. Physiological factors or health conditions that bring about irregular heartbeats and arrythmias could be a possible cause for gaps in the data as well.

Filtering out "NO DATA" and the missing values can give a false idea that the heart rate was steady when it really wasn’t. It might make the average, max, and standard deviation seem better than they actually are, hiding important changes or irregularities. Missing periods could be a sign of a health issue or a problem with the device. Removing them makes analysis easier, but it could mean losing significant information and not getting the full picture of what’s really going on.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

Answer:
Based on the visualization and the metrics, the phase with the lowest maximum heart rate is phase0, with a maximum of 93.0 bpm, followed closely by phase3 with a maximum heart rate of 99.0bpm.

Phase0 has the most stable heart rate with some fluctuations, reflective of a normal sleep pattern. Therefore, based on the lower maximum heart rate, phase0 corresponds to the sleep phase.

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

Answer:
Examining the maximum heart rate values, phase1 and phase2 has the highest maximum at 110.0bpm and 117.0 bpm respectively, which is significantly higher than the other phases.

Therefore, based on the higher maximum heart rate observed in these phases and their pattern of distribution on the line graph, it appears that the exercise phase covers both phase1 and phase2.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Answer:
During regular periods of awake activity, we expect the average heart rate of a phase to be relatively lower than the average heart rate of other phases, but we also expect the standard deviation to be higher.

From the output, the phase with the relatively lower average heart rate and higher standard deviation is phase3 with an average of 60.65 bpm, standard deviation of 11.0
This indicates that phase3 corresponds to the regular awake activity phase.