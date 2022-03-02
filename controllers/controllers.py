from odoo import models, fields, api

class cliente(models.Model):
    _name = 'alquiler.cliente'
    _description = 'Características del cliente'
    _order = 'id'

    id = fields.Integer('id', required = True)
    name = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    telefono = fields.Integer('id', required = True, size=9)
    dni = fields.Char('DNI', required=True, size=9)
    edad = fields.Integer('id')
    direccion = fields.Char('dirección')
    email = fields.Char('Email')
    
    alquiler_id = fields.Many2one(
        'alquiler.alquiler', 'cliente_ids', string='Alquiler')


class alquiler(models.Model):
    _name = 'alquiler.alquiler'
    _description = 'Relación entre cliente y vehiculo'

    id = fields.Integer('id', required = True)
    cliente_id = fields.Integer('id', required = True) 
    vehiculo_id = fields.Integer('id', required = True)
    fecha_entrega = fields.Date('fecha de entrega', required = True, default = fields.date.today())
    fecha_devolucion = fields.Date('fecha de devolucion', required = True)
    devuelto = fields.Boolean(string="Devuelto", required = True, default=False)
    precio = fields.Integer('precio', required = True, help='coste de alquiler por día')

    cliente_ids = fields.One2many(
        'alquiler.cliente', string='Cliente')

    vehiculo_ids = fields.Many2many(
       'alquiler.vehiculo', string='Vehiculo')


class vehiculo(models.Model):
    _name = 'alquiler.vehiculo'
    _description = 'Definición del vehiculo'
    _order = 'name'

    name = fields.Char('Matrícula', required=True, size=7)
    modelo = fields.Char(String='Modelo', required=True)
    construido = fields.Date(string='fecha de fabricación')
    consumo = fields.Float('Consumo', (3,1), default=6.0, help='consumo medio cada 100km')
    descripción = fields.Text('Descripción')

    vehiculo_ids = fields.Many2many(
       'alquiler.alquiler', string='Alquiler')
