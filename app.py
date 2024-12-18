from flask import Flask, render_template, request 

app = Flask(__name__)

Jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        # 'salary': '$130,000'
    },
    {
        'id': 5,
        'title': 'Software Engineer',
        'location': 'San Francisco, USA',
        'salary': '$140,000'
    },
  {
        'id': 6,
        'title': 'Data Engineer',
        'location': 'San Francisco, USA',
        'salary': '$150,000'
  
  }, 
  {
        'id': 7,
        'title': 'DevOPS Expert',
        'location': 'San Francisco, USA',
        'salary': '$160,000'
  
  },
  {
        'id': 8,
        'title': 'Software Engineer',
        'location': 'London',
        'salary': '$170,000'
  
  }
]

@app.route("/")
def index():
    return render_template('index.html', jobs=Jobs[:5], offset=5, total_jobs=len(Jobs), more=False)

@app.route("/more-jobs")
def load_more_jobs():
    offset = int(request.args.get('offset', 5))  # Get the offset from the query parameters
    more_jobs = Jobs[offset:offset+5]  # Return the next 5 jobs
    return render_template(
        'index.html', 
        jobs=more_jobs, 
        offset=offset + 5, 
        total_jobs=len(Jobs),
        more=True  # Set a flag to display "More Jobs" heading
    )

# @app.route("/api/jobs")
# def list_jobs():
#   return jsonify('jobs')
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
