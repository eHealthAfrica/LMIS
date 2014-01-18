# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacilityType'
        db.create_table('facilities_facilitytype', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_facilitytype_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_facilitytype_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(to=orm['facilities.FacilityType'], blank=True, null=True, related_name='sub_facility_types')),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('facilities', ['FacilityType'])

        # Adding model 'Facility'
        db.create_table('facilities_facility', (
            ('company_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['core.Company'], unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('facility_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.FacilityType'])),
            ('supplies_others', self.gf('django.db.models.fields.BooleanField')()),
            ('sdp', self.gf('django.db.models.fields.BooleanField')()),
            ('global_location_no', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('catchment_population', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Location'], null=True)),
            ('has_electricity', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('is_online', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('has_electronic_scc', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('has_electronic_dar', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(default=True, blank=True, null=True)),
            ('go_live_date', self.gf('django.db.models.fields.DateField')()),
            ('go_down_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('is_satellite', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(to=orm['facilities.Facility'], blank=True, null=True, related_name='child_facilities')),
            ('virtual_facility', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('facilities', ['Facility'])

        # Adding M2M table for field facility_operators on 'Facility'
        m2m_table_name = db.shorten_name('facilities_facility_facility_operators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('facility', models.ForeignKey(orm['facilities.facility'], null=False)),
            ('company', models.ForeignKey(orm['core.company'], null=False))
        ))
        db.create_unique(m2m_table_name, ['facility_id', 'company_id'])

        # Adding model 'WarehouseType'
        db.create_table('facilities_warehousetype', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_warehousetype_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_warehousetype_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('facilities', ['WarehouseType'])

        # Adding model 'Warehouse'
        db.create_table('facilities_warehouse', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_warehouse_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_warehouse_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=55, unique=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('is_refrigerated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cold_storage_gross_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('cold_storage_net_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('ambient_storage_gross_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('ambient_storage_net_capacity', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
        ))
        db.send_create_signal('facilities', ['Warehouse'])

        # Adding model 'FacilitySupportedProgram'
        db.create_table('facilities_facilitysupportedprogram', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_facilitysupportedprogram_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_facilitysupportedprogram_modified_by')),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partners.Program'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
        ))
        db.send_create_signal('facilities', ['FacilitySupportedProgram'])

        # Adding model 'FacilitySupportedProgramProduct'
        db.create_table('facilities_facilitysupportedprogramproduct', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_facilitysupportedprogramproduct_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_facilitysupportedprogramproduct_modified_by')),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('program_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partners.ProgramProduct'])),
            ('allocation_info', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partners.ProgramProductAllocationInfo'], unique=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.OrderGroup'])),
        ))
        db.send_create_signal('facilities', ['FacilitySupportedProgramProduct'])

        # Adding model 'SupervisoryNode'
        db.create_table('facilities_supervisorynode', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_supervisorynode_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_supervisorynode_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(to=orm['facilities.SupervisoryNode'], blank=True, null=True, related_name='parent_supervisory_node')),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.Facility'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('facilities', ['SupervisoryNode'])

        # Adding model 'OrderGroup'
        db.create_table('facilities_ordergroup', (
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_ordergroup_created_by')),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True, related_name='facilities_ordergroup_modified_by')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('supervisory_node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facilities.SupervisoryNode'])),
        ))
        db.send_create_signal('facilities', ['OrderGroup'])

        # Adding M2M table for field member_facilities on 'OrderGroup'
        m2m_table_name = db.shorten_name('facilities_ordergroup_member_facilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ordergroup', models.ForeignKey(orm['facilities.ordergroup'], null=False)),
            ('facility', models.ForeignKey(orm['facilities.facility'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ordergroup_id', 'facility_id'])


    def backwards(self, orm):
        # Deleting model 'FacilityType'
        db.delete_table('facilities_facilitytype')

        # Deleting model 'Facility'
        db.delete_table('facilities_facility')

        # Removing M2M table for field facility_operators on 'Facility'
        db.delete_table(db.shorten_name('facilities_facility_facility_operators'))

        # Deleting model 'WarehouseType'
        db.delete_table('facilities_warehousetype')

        # Deleting model 'Warehouse'
        db.delete_table('facilities_warehouse')

        # Deleting model 'FacilitySupportedProgram'
        db.delete_table('facilities_facilitysupportedprogram')

        # Deleting model 'FacilitySupportedProgramProduct'
        db.delete_table('facilities_facilitysupportedprogramproduct')

        # Deleting model 'SupervisoryNode'
        db.delete_table('facilities_supervisorynode')

        # Deleting model 'OrderGroup'
        db.delete_table('facilities_ordergroup')

        # Removing M2M table for field member_facilities on 'OrderGroup'
        db.delete_table(db.shorten_name('facilities_ordergroup_member_facilities'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_address_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_address_modified_by'"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'subdivision': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'core.company': {
            'Meta': {'ordering': "['name']", 'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Address']", 'blank': 'True', 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.CompanyCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Contact']", 'blank': 'True', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_company_created_by'"}),
            'footer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_company_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Product']", 'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_companycategory_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_companycategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.CompanyCategory']", 'blank': 'True', 'null': 'True', 'related_name': "'core_companycategory_sub_company_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.contact': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Contact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_contact_created_by'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'irc': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_contact_modified_by'"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'sip': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'core.currency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_currency_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_currency_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'symbol_position': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '20'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UnitOfMeasurement']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductCategory']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_product_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_product_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_productcategory_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_productcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.ProductCategory']", 'blank': 'True', 'null': 'True', 'related_name': "'sub_product_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.unitofmeasurement': {
            'Meta': {'ordering': "['name']", 'object_name': 'UnitOfMeasurement'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_unitofmeasurement_created_by'"}),
            'factor': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_unitofmeasurement_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'rounding_precision': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True', 'null': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uom_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UOMCategory']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'core.uomcategory': {
            'Meta': {'object_name': 'UOMCategory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_uomcategory_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'core_uomcategory_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['core.UOMCategory']", 'blank': 'True', 'null': 'True', 'related_name': "'core_uomcategory_sub_uom_categories'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.facility': {
            'Meta': {'_ormbases': ['core.Company'], 'object_name': 'Facility'},
            'catchment_population': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'company_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['core.Company']", 'unique': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'facility_operators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']", 'blank': 'True', 'null': 'True', 'related_name': "'facility_operators'"}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.FacilityType']"}),
            'global_location_no': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'go_down_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'go_live_date': ('django.db.models.fields.DateField', [], {}),
            'has_electricity': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'has_electronic_dar': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'has_electronic_scc': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'blank': 'True', 'null': 'True'}),
            'is_online': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'is_satellite': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.Facility']", 'blank': 'True', 'null': 'True', 'related_name': "'child_facilities'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sdp': ('django.db.models.fields.BooleanField', [], {}),
            'supplies_others': ('django.db.models.fields.BooleanField', [], {}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'virtual_facility': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'facilities.facilitysupportedprogram': {
            'Meta': {'object_name': 'FacilitySupportedProgram'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_facilitysupportedprogram_created_by'"}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_facilitysupportedprogram_modified_by'"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Program']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.facilitysupportedprogramproduct': {
            'Meta': {'object_name': 'FacilitySupportedProgramProduct'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allocation_info': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['partners.ProgramProductAllocationInfo']", 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_facilitysupportedprogramproduct_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_facilitysupportedprogramproduct_modified_by'"}),
            'order_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.OrderGroup']"}),
            'program_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.ProgramProduct']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_facilitytype_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_facilitytype_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.FacilityType']", 'blank': 'True', 'null': 'True', 'related_name': "'sub_facility_types'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.ordergroup': {
            'Meta': {'object_name': 'OrderGroup'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_ordergroup_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'member_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['facilities.Facility']", 'blank': 'True', 'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_ordergroup_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'supervisory_node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.SupervisoryNode']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.supervisorynode': {
            'Meta': {'object_name': 'SupervisoryNode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_supervisorynode_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_supervisorynode_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['facilities.SupervisoryNode']", 'blank': 'True', 'null': 'True', 'related_name': "'parent_supervisory_node'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'ambient_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'ambient_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55', 'unique': 'True'}),
            'cold_storage_gross_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'cold_storage_net_capacity': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_warehouse_created_by'"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facilities.Facility']"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_refrigerated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_warehouse_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'facilities.warehousetype': {
            'Meta': {'object_name': 'WarehouseType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_warehousetype_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'facilities_warehousetype_modified_by'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'alt_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['locations.Location']", 'null': 'True', 'related_name': "'children'"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'})
        },
        'partners.program': {
            'Meta': {'object_name': 'Program'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'partners_program_created_by'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'partners_program_modified_by'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'unique': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'partners.programproduct': {
            'Meta': {'object_name': 'ProgramProduct'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'partners_programproduct_created_by'"}),
            'current_price_per_unit': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '21'}),
            'funding_source': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Company']"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'partners_programproduct_modified_by'"}),
            'price_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']", 'blank': 'True', 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['partners.Program']"}),
            'unit_per_target': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        'partners.programproductallocationinfo': {
            'Meta': {'object_name': 'ProgramProductAllocationInfo'},
            'adjustment_value': ('django.db.models.fields.IntegerField', [], {}),
            'buffer_percentage': ('django.db.models.fields.FloatField', [], {}),
            'coverage_rate': ('django.db.models.fields.FloatField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'partners_programproductallocationinfo_created_by'"}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lead_time': ('django.db.models.fields.IntegerField', [], {}),
            'max_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'min_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True', 'related_name': "'partners_programproductallocationinfo_modified_by'"}),
            'push': ('django.db.models.fields.BooleanField', [], {}),
            'supply_interval': ('django.db.models.fields.IntegerField', [], {}),
            'target_population': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'wastage_rate': ('django.db.models.fields.FloatField', [], {}),
            'who_ratio': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['facilities']