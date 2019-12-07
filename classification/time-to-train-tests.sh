#Face Bayes
printf "%s\n" "Face Bayes" >> time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> time-to-train.txt
  for i in {1..5}; do
    python ReadData.py $"-f" $"-b" $c
  done
done


#Digit Bayes
printf "\n%s\n" "Digit Bayes" >> time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> time-to-train.txt
  for i in {1..5}; do
    python ReadData.py $"-d" $"-b" $c
  done
done


#Face Perceptron
printf "\n%s\n" "Face Perceptron" >>  time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >>  time-to-train.txt
  for i in {1..5}; do
    python ReadData.py $"-f" $"-p" $c
  done
done


#Digit Perceptron
printf "\n%s\n" "Digit Perceptron" >> time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> time-to-train.txt
  for i in {1..5}; do
    python ReadData.py $"-d" $"-p" $c
  done
done


#Face K-Nearest
printf "\n%s\n" "Face K-Nearest" >> time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> time-to-train.txt
  for i in {1..5}; do
    python ReadData.py $"-f" $"-k" $c
  done
done


#Digit K-Nearest
printf "\n%s\n" "Digit K-Nearest" >> time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> time-to-train.txt
  for i in {1..5}; do
    python ReadData.py $"-d" $"-k" $c
  done
done