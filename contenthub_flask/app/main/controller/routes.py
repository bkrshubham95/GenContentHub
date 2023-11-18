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
    """
    Saves the user feedback to a csv file for retratining

    Args: json 

    return: Ok - success
    """
    data = request.get_json()
    slogan = data.get('slogan' , '')
    modes = data.get('modes' , '')
    keywords = data.get('keywords' , '')


    data_to_append = [
        [slogan, k, modes[k] , keywords] for k in modes
    ]

    # File path
    file_path = 'retraing_data.csv'

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        for row in data_to_append:
            writer.writerow(row)


    return jsonify({"status" : "OK"})


@main.route('/process-words', methods=['POST'])
def process_words():
    data = request.get_json()
    words = data.get('words' , '')
    modes = data.get('modes' , '')
    print(words , data , modes)
    return generate_response(words)
    # # Process the words here
    # processed_data = {'processed_words': words}
    # return jsonify(processed_data)


def generate_response(words):
    """
    
    Generates slogans from from the wwords

    Args: List of words 

    return: JSON
    """
    global model
    
    try:
        if  words:
            system_message = "You are a helpful assistant"
            user_message = "Generate a list of 5 slogan using " + " ".join(words) + " without explanation"
            max_tokens = 300

            # Prompt creation
            prompt = f"""<s>[INST] <<SYS>>
            {system_message}
            <</SYS>>
            {user_message} [/INST]"""
            
            if model is None:
                model_path = "llama-2-7b-chat.Q2_K.gguf"
                
                model = Llama(model_path=model_path)
             
            # Run the model
            output = model(prompt, max_tokens=max_tokens, echo=True)
            text_data = output['choices'][0]['text']

            start_index = text_data.find('1. "')

            slogans_text = text_data[start_index:]
            slogans = slogans_text.split('\n')

            cleaned_slogans = [slogan.strip() for slogan in slogans if slogan.strip()]
            processed_data = {'processed_words': cleaned_slogans}
            return jsonify(processed_data)

        else:
            return jsonify({"error": "Missing required parameters"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@main.route('/', methods=['GET'])
def index():
    """
    Just to test the page load 
    """
    return "Welcome to the main page"  
