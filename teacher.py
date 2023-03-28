from flask import*
from database import DB,CR
teacher=Blueprint("teacher",__name__)

@teacher.route("/")
def TeacherHome():
  return render_template("teacherhome.html")

@teacher.route("/answerquestion",methods=["post","get"])
def AnswerQuestion():
  CR.execute("SELECT * FROM smdb")
  smdb=CR.fetchall()
  if 'submit' in request.form:
    answer = request.form['ans']
    id = request.form['submit']
    sql = "UPDATE smdb set answer=%s WHERE id=%s" 
    val = (answer,id)
    CR.execute(sql,val)
    DB.commit()
    flash("Answer Submited")
    return redirect(url_for("teacher.AnswerQuestion"))
  
  return render_template('answerquestion.html',smdb=smdb)

@teacher.route("/deletesmdb",methods=["post","get"])
def deletesmdb():
  CR.execute("SELECT * FROM smdb")
  res=CR.fetchall()
  if "submit" in request.form:
    id=request.form['submit']
    CR.execute("DELETE FROM smdb WHERE id=%s",(id,))
    DB.commit()
    flash("Item Delete")
    return redirect(url_for('teacher.deletesmdb'))
  return render_template('deletesmdb.html',res=res)