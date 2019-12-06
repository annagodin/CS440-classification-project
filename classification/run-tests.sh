#Face Bayes
printf "%s\n" "Face Bayes" >> results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> results.txt
  for i in {1..5}; do
    python ReadData.py $"-f" $"-b" $c
  done
done


#Digit Bayes
printf "\n%s\n" "Digit Bayes" >> results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> results.txt
  for i in {1..5}; do
    python ReadData.py $"-d" $"-b" $c
  done
done


#Face Perceptron
printf "\n%s\n" "Face Perceptron" >> results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> results.txt
  for i in {1..5}; do
    python ReadData.py $"-f" $"-p" $c
  done
done


#Digit Perceptron
printf "\n%s\n" "Digit Perceptron" >> results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> results.txt
  for i in {1..5}; do
    python ReadData.py $"-d" $"-p" $c
  done
done


#Face K-Nearest
printf "\n%s\n" "Face K-Nearest" >> results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> results.txt
  for i in {1..5}; do
    python ReadData.py $"-f" $"-k" $c
  done
done


#Digit K-Nearest
printf "\n%s\n" "Digit K-Nearest" >> results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> results.txt
  for i in {1..5}; do
    python ReadData.py $"-d" $"-k" $c
  done
done