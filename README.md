Prerequisite:
1. Docker
2. MiniKube

Steps to run locally:
1. Clone the repository
2. Navigate to GenContentHub/contenthub_flask and download the model from the link - (https://drive.google.com/file/d/1Qm9cSozYtbaeC83eSsDlmL3L4SctKjOm/view?usp=sharing).
3. run the command  from directory /contenthub_flask/ -> `docker build -t contenthub_flask .`
4. run the command from directory /my-contenthub-app/ -> `docker build -t my-contenthub-app .`
5. run the command from top-level directory where deployemnet.yaml is present -> `kubectl apply -f deployment.yaml`
6. run the command from top-level directory  - > `minikube service my-app`
7. Navigate to the link generated from above command.
8. type a few words with space between each word and the click on send word.
9.  5 slogans will be generated.
10.  select feedback and click sendPhraseFeedback.

