from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from google.appengine.api import namespace_manager, users as google_users
from app import app

@app.before_request
def set_tenant():
  tenant = request.host.split(':')[0].split('.')[0]
  if(tenant == 'www' or tenant == 'localhost'):
    tenant = 'default'
  namespace_manager.set_namespace(tenant)
