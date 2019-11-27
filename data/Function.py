class Function:

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def add_permission(self, client, statement_id, action, principal, **kwargs):
        response = client.add_permission(
            FunctionName=self.FunctionName,
            StatementId=statement_id,
            Action=action,
            Principal=principal,
            **kwargs
        )

        return response

    def create_alias(self, client, name, function_version, **kwargs):
        response = client.create_alias(
            FunctionName=self.FunctionName,
            Name=name,
            FunctionVersion=function_version,
            **kwargs
        )

        return response

    def delete_alias(self, client, name):
        response = client.delete_alias(
            FunctionName=self.FunctionName,
            Name=name
        )

        return response

    def delete_function(self, client):
        response = client.delete_function(
            FunctionName=self.FunctionName
        )

        return response

    def publish_version(self, client, **kwargs):
        response = client.publish_version(
            FunctionName=self.FunctionName,
            **kwargs
        )

        return response

    def put_function_concurrency(self, client, reserved_concurrent_executions):
        response = client.put_function_concurrency(
            FunctionName=self.FunctionName,
            ReservedFunctionConcurrency=reserved_concurrent_executions
        )

        return response

    def remove_layer_version_permission(self, client, layer_name, version_number, statement_id, **kwargs):
        response = client.remove_layer_version_permission(
            FunctionName=self.FunctionName,
            LayerName=layer_name,
            VersionNumber=version_number,
            StatementId=statement_id,
            **kwargs
        )

        return response

    def remove_permission(self, client, statement_id, **kwargs):
        response = client.remove_permission(
            FunctionName=self.FunctionName,
            StatementId=statement_id,
            **kwargs
        )

        return response

    def invoke(self, client, **kwargs):
        response = client.invoke(
            FunctionName=self.FunctionName,
            **kwargs
        )

        return response
