from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def score_server():

    try:
        error_msg = ''
        #read the score file
        read_current_score = open('/WorldofGames/Scores.txt', 'r') 
        get_currentt_score = read_current_score.readlines()
        length = len(get_currentt_score)

        final_score = 0
        #sum the current score
        for x in range(0, length-1):
            sum_of_my_score = int(get_currentt_score[x].split('=', 1)[1])
            print(sum_of_my_score)
            final_score += sum_of_my_score
        read_current_score.close()
    #handle the error if there is any problem when reading the score file
    except EnvironmentError as error:
        error_msg=error
        print('Could not open/read file' , error)

    if(error_msg):
        return render_template('error.html', content=error_msg)
    else:
        return render_template('index.html', content=final_score)

app.run(port=8001,host="0.0.0.0", debug=True)
