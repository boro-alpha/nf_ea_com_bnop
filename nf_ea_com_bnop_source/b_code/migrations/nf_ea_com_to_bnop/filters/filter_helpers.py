import sys
import pandas
from nf_common_source.code.nf.types.nf_column_types import NfColumnTypes
from nf_common_source.code.services.reporting_service.reporters.log_with_datetime import log_message
from nf_ea_common_tools_source.b_code.services.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import NfEaComColumnTypes


def get_ea_object_nf_uuid_by_its_ea_guid(
        ea_objects: pandas.DataFrame,
        stereotype_ea_guid: str) \
        -> str:
    object_row = \
        ea_objects[ea_objects[NfEaComColumnTypes.EXPLICIT_OBJECTS_EA_GUID.column_name] == stereotype_ea_guid]

    object_nf_uuids = \
        object_row[NfColumnTypes.NF_UUIDS.column_name].values

    if len(object_nf_uuids) == 0:
        sys.exit(-1)

    if len(object_nf_uuids) > 1:
        log_message(
            message='Multiple connectors with guid ' + stereotype_ea_guid)

    object_nf_uuid = \
        object_nf_uuids[0]

    return \
        object_nf_uuid
