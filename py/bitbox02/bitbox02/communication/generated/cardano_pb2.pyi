# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .common_pb2 import (
    Keypath as common_pb2___Keypath,
    PubResponse as common_pb2___PubResponse,
)

from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CardanoNetwork(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> CardanoNetwork: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[CardanoNetwork]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, CardanoNetwork]]: ...
    CardanoMainnet = typing___cast(CardanoNetwork, 0)
    CardanoTestnet = typing___cast(CardanoNetwork, 1)
CardanoMainnet = typing___cast(CardanoNetwork, 0)
CardanoTestnet = typing___cast(CardanoNetwork, 1)

class CardanoXpubsRequest(google___protobuf___message___Message):

    @property
    def keypaths(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[common_pb2___Keypath]: ...

    def __init__(self,
        *,
        keypaths : typing___Optional[typing___Iterable[common_pb2___Keypath]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoXpubsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"keypaths"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"keypaths",b"keypaths"]) -> None: ...

class CardanoXpubsResponse(google___protobuf___message___Message):
    xpubs = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]

    def __init__(self,
        *,
        xpubs : typing___Optional[typing___Iterable[bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoXpubsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"xpubs"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"xpubs",b"xpubs"]) -> None: ...

class CardanoScriptConfig(google___protobuf___message___Message):
    class PkhSkh(google___protobuf___message___Message):
        keypath_payment = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
        keypath_stake = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

        def __init__(self,
            *,
            keypath_payment : typing___Optional[typing___Iterable[int]] = None,
            keypath_stake : typing___Optional[typing___Iterable[int]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CardanoScriptConfig.PkhSkh: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"keypath_payment",u"keypath_stake"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"keypath_payment",b"keypath_payment",u"keypath_stake",b"keypath_stake"]) -> None: ...


    @property
    def pkh_skh(self) -> CardanoScriptConfig.PkhSkh: ...

    def __init__(self,
        *,
        pkh_skh : typing___Optional[CardanoScriptConfig.PkhSkh] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoScriptConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"config",u"pkh_skh"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",u"pkh_skh"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"config",b"config",u"pkh_skh",b"pkh_skh"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"pkh_skh",b"pkh_skh"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"config",b"config"]) -> typing_extensions___Literal["pkh_skh"]: ...

class CardanoAddressRequest(google___protobuf___message___Message):
    network = ... # type: CardanoNetwork
    display = ... # type: bool

    @property
    def script_config(self) -> CardanoScriptConfig: ...

    def __init__(self,
        *,
        network : typing___Optional[CardanoNetwork] = None,
        display : typing___Optional[bool] = None,
        script_config : typing___Optional[CardanoScriptConfig] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoAddressRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"display",u"network",u"script_config"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"script_config",b"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"display",b"display",u"network",b"network",u"script_config",b"script_config"]) -> None: ...

class CardanoSignTransactionRequest(google___protobuf___message___Message):
    class Input(google___protobuf___message___Message):
        keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
        prev_out_hash = ... # type: bytes
        prev_out_index = ... # type: int

        def __init__(self,
            *,
            keypath : typing___Optional[typing___Iterable[int]] = None,
            prev_out_hash : typing___Optional[bytes] = None,
            prev_out_index : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CardanoSignTransactionRequest.Input: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"keypath",u"prev_out_hash",u"prev_out_index"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"keypath",b"keypath",u"prev_out_hash",b"prev_out_hash",u"prev_out_index",b"prev_out_index"]) -> None: ...

    class Output(google___protobuf___message___Message):
        encoded_address = ... # type: typing___Text
        value = ... # type: int

        @property
        def script_config(self) -> CardanoScriptConfig: ...

        def __init__(self,
            *,
            encoded_address : typing___Optional[typing___Text] = None,
            value : typing___Optional[int] = None,
            script_config : typing___Optional[CardanoScriptConfig] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CardanoSignTransactionRequest.Output: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"script_config"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"encoded_address",u"script_config",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"script_config",b"script_config"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"encoded_address",b"encoded_address",u"script_config",b"script_config",u"value",b"value"]) -> None: ...

    class Certificate(google___protobuf___message___Message):
        class StakeDelegation(google___protobuf___message___Message):
            keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
            pool_keyhash = ... # type: bytes

            def __init__(self,
                *,
                keypath : typing___Optional[typing___Iterable[int]] = None,
                pool_keyhash : typing___Optional[bytes] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> CardanoSignTransactionRequest.Certificate.StakeDelegation: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"keypath",u"pool_keyhash"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[u"keypath",b"keypath",u"pool_keyhash",b"pool_keyhash"]) -> None: ...


        @property
        def stake_registration(self) -> common_pb2___Keypath: ...

        @property
        def stake_deregistration(self) -> common_pb2___Keypath: ...

        @property
        def stake_delegation(self) -> CardanoSignTransactionRequest.Certificate.StakeDelegation: ...

        def __init__(self,
            *,
            stake_registration : typing___Optional[common_pb2___Keypath] = None,
            stake_deregistration : typing___Optional[common_pb2___Keypath] = None,
            stake_delegation : typing___Optional[CardanoSignTransactionRequest.Certificate.StakeDelegation] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CardanoSignTransactionRequest.Certificate: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"cert",u"stake_delegation",u"stake_deregistration",u"stake_registration"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"cert",u"stake_delegation",u"stake_deregistration",u"stake_registration"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"cert",b"cert",u"stake_delegation",b"stake_delegation",u"stake_deregistration",b"stake_deregistration",u"stake_registration",b"stake_registration"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"cert",b"cert",u"stake_delegation",b"stake_delegation",u"stake_deregistration",b"stake_deregistration",u"stake_registration",b"stake_registration"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions___Literal[u"cert",b"cert"]) -> typing_extensions___Literal["stake_registration","stake_deregistration","stake_delegation"]: ...

    class Withdrawal(google___protobuf___message___Message):
        keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
        value = ... # type: int

        def __init__(self,
            *,
            keypath : typing___Optional[typing___Iterable[int]] = None,
            value : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CardanoSignTransactionRequest.Withdrawal: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"keypath",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"keypath",b"keypath",u"value",b"value"]) -> None: ...

    network = ... # type: CardanoNetwork
    fee = ... # type: int
    ttl = ... # type: int
    validity_interval_start = ... # type: int

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CardanoSignTransactionRequest.Input]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CardanoSignTransactionRequest.Output]: ...

    @property
    def certificates(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CardanoSignTransactionRequest.Certificate]: ...

    @property
    def withdrawals(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CardanoSignTransactionRequest.Withdrawal]: ...

    def __init__(self,
        *,
        network : typing___Optional[CardanoNetwork] = None,
        inputs : typing___Optional[typing___Iterable[CardanoSignTransactionRequest.Input]] = None,
        outputs : typing___Optional[typing___Iterable[CardanoSignTransactionRequest.Output]] = None,
        fee : typing___Optional[int] = None,
        ttl : typing___Optional[int] = None,
        certificates : typing___Optional[typing___Iterable[CardanoSignTransactionRequest.Certificate]] = None,
        withdrawals : typing___Optional[typing___Iterable[CardanoSignTransactionRequest.Withdrawal]] = None,
        validity_interval_start : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoSignTransactionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"certificates",u"fee",u"inputs",u"network",u"outputs",u"ttl",u"validity_interval_start",u"withdrawals"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"certificates",b"certificates",u"fee",b"fee",u"inputs",b"inputs",u"network",b"network",u"outputs",b"outputs",u"ttl",b"ttl",u"validity_interval_start",b"validity_interval_start",u"withdrawals",b"withdrawals"]) -> None: ...

class CardanoSignTransactionResponse(google___protobuf___message___Message):
    class ShelleyWitness(google___protobuf___message___Message):
        public_key = ... # type: bytes
        signature = ... # type: bytes

        def __init__(self,
            *,
            public_key : typing___Optional[bytes] = None,
            signature : typing___Optional[bytes] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CardanoSignTransactionResponse.ShelleyWitness: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"public_key",u"signature"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"public_key",b"public_key",u"signature",b"signature"]) -> None: ...


    @property
    def shelley_witnesses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CardanoSignTransactionResponse.ShelleyWitness]: ...

    def __init__(self,
        *,
        shelley_witnesses : typing___Optional[typing___Iterable[CardanoSignTransactionResponse.ShelleyWitness]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoSignTransactionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"shelley_witnesses"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"shelley_witnesses",b"shelley_witnesses"]) -> None: ...

class CardanoRequest(google___protobuf___message___Message):

    @property
    def xpubs(self) -> CardanoXpubsRequest: ...

    @property
    def address(self) -> CardanoAddressRequest: ...

    @property
    def sign_transaction(self) -> CardanoSignTransactionRequest: ...

    def __init__(self,
        *,
        xpubs : typing___Optional[CardanoXpubsRequest] = None,
        address : typing___Optional[CardanoAddressRequest] = None,
        sign_transaction : typing___Optional[CardanoSignTransactionRequest] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"address",u"request",u"sign_transaction",u"xpubs"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address",u"request",u"sign_transaction",u"xpubs"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"address",b"address",u"request",b"request",u"sign_transaction",b"sign_transaction",u"xpubs",b"xpubs"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address",b"address",u"request",b"request",u"sign_transaction",b"sign_transaction",u"xpubs",b"xpubs"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"request",b"request"]) -> typing_extensions___Literal["xpubs","address","sign_transaction"]: ...

class CardanoResponse(google___protobuf___message___Message):

    @property
    def xpubs(self) -> CardanoXpubsResponse: ...

    @property
    def pub(self) -> common_pb2___PubResponse: ...

    @property
    def sign_transaction(self) -> CardanoSignTransactionResponse: ...

    def __init__(self,
        *,
        xpubs : typing___Optional[CardanoXpubsResponse] = None,
        pub : typing___Optional[common_pb2___PubResponse] = None,
        sign_transaction : typing___Optional[CardanoSignTransactionResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CardanoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"pub",u"response",u"sign_transaction",u"xpubs"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"pub",u"response",u"sign_transaction",u"xpubs"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"pub",b"pub",u"response",b"response",u"sign_transaction",b"sign_transaction",u"xpubs",b"xpubs"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"pub",b"pub",u"response",b"response",u"sign_transaction",b"sign_transaction",u"xpubs",b"xpubs"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"response",b"response"]) -> typing_extensions___Literal["xpubs","pub","sign_transaction"]: ...