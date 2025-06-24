from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Incident, User
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    if current_user.role == 'admin':
        incidents = Incident.query.all()
    elif current_user.role == 'engineer':
        incidents = Incident.query.filter_by(assigned_to=current_user.username).all()
    else:
        incidents = Incident.query.filter_by(reported_by=current_user.username).all()
    users = User.query.all()
    return render_template('dashboard.html', incidents=incidents, users=users)

@main.route('/incident/create', methods=['GET', 'POST'])
@login_required
def create_incident():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        incident = Incident(title=title, description=description, priority=priority, reported_by=current_user.username)
        db.session.add(incident)
        db.session.commit()
        flash("Incident created successfully.")
        return redirect(url_for('main.home'))
    return render_template('create_incident.html')

@main.route('/incident/assign/<int:id>', methods=['POST'])
@login_required
def assign_incident(id):
    if current_user.role != 'admin':
        flash("Unauthorized")
        return redirect(url_for('main.home'))
    engineer = request.form['engineer']
    incident = Incident.query.get(id)
    incident.assigned_to = engineer
    incident.status = "In Progress"
    db.session.commit()
    flash("Incident assigned.")
    return redirect(url_for('main.home'))

@main.route('/incident/resolve/<int:id>')
@login_required
def resolve_incident(id):
    incident = Incident.query.get(id)
    if current_user.role not in ['admin', 'engineer']:
        flash("Unauthorized")
        return redirect(url_for('main.home'))
    if current_user.username != incident.assigned_to and current_user.role != 'admin':
        flash("Only assigned engineer or admin can resolve.")
        return redirect(url_for('main.home'))
    incident.status = "Resolved"
    incident.resolved_at = datetime.utcnow()
    db.session.commit()
    flash("Incident marked as resolved.")
    return redirect(url_for('main.home'))
