from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao = SubmitField("Fazer login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário não cadastrado, faça um cadastro para continuar")

class FormCriarConta(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuaário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado, faça login para continuar")
        
    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError("Nome de usuário já cadastrado, escolha outro")
        
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")
    