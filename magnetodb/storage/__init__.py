# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from magnetodb.common import config
from magnetodb.openstack.common import importutils

CONF = config.CONF
STORAGE_IMPL = importutils.import_module(CONF.storage_impl)


def create_table(context, table_schema):
    """
    Creates table

    @param context: current request context
    @param table_schema: TableSchema instance which define table to create

    @raise BackendInteractionException
    """
    STORAGE_IMPL.create_table(context, table_schema)


def delete_table(context, table_name):
    """
    Creates table

    @param context: current request context
    @param table_name: String, name of table to delete

    @raise BackendInteractionException
    """
    STORAGE_IMPL.delete_table(context, table_name)


def describe_table(context, table_name):
    """
    Creates table

    @param context: current request context
    @param table_name: String, name of table to describes

    @return: TableSchema instance

    @raise BackendInteractionException
    """
    return STORAGE_IMPL.describe_table(context, table_name)


def list_tables(context, exclusive_start_table_name=None, limit=None):
    """
    @param context: current request context
    @param exclusive_start_table_name
    @param limit: limit of returned table names
    @return list of table names

    @raise BackendInteractionException
    """
    return STORAGE_IMPL.list_tables(context, exclusive_start_table_name, limit)


def put_item(context, put_request, if_not_exist=False,
             expected_condition_map=None):
    """
    @param context: current request context
    @param put_request: contains PutItemRequest items to perform
                put item operation
    @param if_not_exist: put item only is row is new record (It is possible to
                use only one of if_not_exist and expected_condition_map
                parameter)
    @param expected_condition_map: expected attribute name to
                ExpectedCondition instance mapping. It provides preconditions
                to make decision about should item be put or not

    @return: True if operation performed, otherwise False

    @raise BackendInteractionException
    """
    return STORAGE_IMPL.put_item(context, put_request, if_not_exist,
                                 expected_condition_map)


def delete_item(context, delete_request, expected_condition_map=None):
    """
    @param context: current request context
    @param delete_request: contains DeleteItemRequest items to perform
                delete item operation
    @param expected_condition_map: expected attribute name to
                ExpectedCondition instance mapping. It provides preconditions
                to make decision about should item be deleted or not

    @return: True if operation performed, otherwise False (if operation was
                skipped by out of date timestamp, it is considered as
                successfully performed)

    @raise BackendInteractionException
    """
    return STORAGE_IMPL.delete_item(context, delete_request,
                                    expected_condition_map)


def execute_write_batch(context, write_request_list, durable=True):
    """
    @param context: current request context
    @param write_request_list: contains WriteItemBatchableRequest items to
                perform batch
    @param durable: if True, batch will be fully performed or fully skipped.
                Partial batch execution isn't allowed

    @raise BackendInteractionException
    """
    STORAGE_IMPL.execute_write_batch(context, write_request_list, durable)


def update_item(context, table_name, key_attribute_map, attribute_action_map,
                expected_condition_map=None):
    """
    @param context: current request context
    @param table_name: String, name of table to delete item from
    @param key_attribute_map: key attribute name to
                AttributeValue mapping. It defines row it to update item
    @param attribute_action_map: attribute name to UpdateItemAction instance
                mapping. It defines actions to perform for each given attribute
    @param expected_condition_map: expected attribute name to
                ExpectedCondition instance mapping. It provides preconditions
                to make decision about should item be updated or not
    @return: True if operation performed, otherwise False

    @raise BackendInteractionException
    """
    return STORAGE_IMPL.update_item(context, table_name, key_attribute_map,
                                    attribute_action_map,
                                    expected_condition_map)


def select_item(context, table_name, indexed_condition_map,
                attributes_to_get=None, limit=None, consistent=True):
    """
    @param context: current request context
    @param table_name: String, name of table to get item from
    @param indexed_condition_map: indexed attribute name to
                IndexedCondition instance mapping. It defines rows
                set to be selected
    @param attributes_to_get: attribute name list to get. If not specified, all
                attributes should be returned. Also aggregate functions are
                allowed, if they are supported by storage implementation

    @param limit: maximum count of returned values
    @param consistent: define is operation consistent or not (by default it is
                not consistent)

    @return list of attribute name to AttributeValue mappings

    @raise BackendInteractionException
    """
    return STORAGE_IMPL.select_item(context, table_name, indexed_condition_map,
                                    attributes_to_get, limit, consistent)
