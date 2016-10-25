from rest_framework import schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
	generator = schemas.SchemaGenerator(title='E-Commerce API')
	return Response(generator.get_schema(request=request))