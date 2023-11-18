# app/main/controller/routes.py
from flask import jsonify, Blueprint, request
from app.main import main
from llama_cpp import Llama
import csv
from flask_cors import CORS  


model =None

main = Blueprint('main', __name__)
CORS(main)



@main.route('/dump-feedback', methods=['POST'])
def dump_feedback():
    data = request.get_json()
    slogan = data.get('slogan' , '')
    modes = data.get('modes' , '')
    keywords = data.get('keywords' , '')


    data_to_append = [
        [slogan, k, modes[k] , keywords] for k in modes
    ]

    # File path
    file_path = 'your_file.csv'

    # Open the file in append mode and create a CSV writer object
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Append each row of data
        for row in data_to_append:
            writer.writerow(row)


    return jsonify({"status" : "OK"})


@main.route('/process-words', methods=['POST'])
def process_words():
    #return jsonify("hello world")
    data = request.get_json()
    words = data.get('words' , '')
    modes = data.get('modes' , '')
    print(words , data , modes)
    return generate_response(words)
    # # Process the words here
    # processed_data = {'processed_words': words}
    # return jsonify(processed_data)


def generate_response(words):
    global model
    
    try:
        # Check if the required fields are present in the JSON data
        if  words:
            system_message = "You are a helpful assistant"
            user_message = "Generate a list of 5 slogan using " + " ".join(words) + " without explanation"
            max_tokens = 300

            # Prompt creation
            prompt = f"""<s>[INST] <<SYS>>
            {system_message}
            <</SYS>>
            {user_message} [/INST]"""
            
            # Create the model if it was not previously created
            if model is None:
                # Put the location of to the GGUF model that you've download from HuggingFace here
                model_path = "llama-2-7b-chat.Q2_K.gguf"
                
                # Create the model
                model = Llama(model_path=model_path)
             
            # Run the model
            output = model(prompt, max_tokens=max_tokens, echo=True)
            text_data = output['choices'][0]['text']
            print(text_data)


            # Find the starting index of the first slogan
            start_index = text_data.find('1. "')

            # Extract the text containing slogans
            slogans_text = text_data[start_index:]

            # Split the text into individual slogans based on the numbering pattern ("1.", "2.", etc.)
            slogans = slogans_text.split('\n')

            # Remove empty elements and strip whitespace from each slogan
            cleaned_slogans = [slogan.strip() for slogan in slogans if slogan.strip()]

            print(cleaned_slogans)
            processed_data = {'processed_words': cleaned_slogans}

            
            
            return jsonify(processed_data)

        else:
            return jsonify({"error": "Missing required parameters"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@main.route('/', methods=['GET'])
def index():
    return "Welcome to the main page"  # Replace this with your desired response
