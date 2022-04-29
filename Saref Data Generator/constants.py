PREAMBLE = """
@prefix saref: <https://saref.etsi.org/core/> .
@prefix om: <http://www.wurvoc.org/vocabularies/om-1.8/> .
@prefix ex: <http://example.com/> .
@prefix smart: <http://example.com/smarthouse/> .

# Addons

<https://interconnectproject.eu/example/> rdf:type owl:Ontology ;
owl:imports <https://saref.etsi.org/core/> ;		
.

om:degree_Celsius rdf:type saref:TemperatureUnit ;
					        rdfs:label "Degree Celsius"
.

ex:OnState rdf:type saref:OnState .
ex:OffState rdf:type saref:OffState .
ex:CloseState rdf:type saref:CloseState .
ex:OpenState rdf:type saref:OpenState .

ex:House rdf:type saref:FeatureOfInterest ;
         rdf:type smart:House ;
.

ex:LivingRoom rdf:type saref:FeatureOfInterest ;
              rdf:type smart:Room 
.
ex:Bedroom rdf:type saref:FeatureOfInterest  ;
              rdf:type smart:Room 
.
ex:Kitchen rdf:type saref:FeatureOfInterest  ;
              rdf:type smart:Room 
.
ex:Entrance rdf:type saref:FeatureOfInterest  ;
              rdf:type smart:Room 
.
ex:Terrace rdf:type saref:FeatureOfInterest  ;
              rdf:type smart:Outdoor 
.
ex:UtilityRoom rdf:type saref:FeatureOfInterest  ;
              rdf:type smart:Room 
.

ex:MainClock rdf:type smart:SmartClock ;
             saref:hasTimestamp "2020-12-02T14:30:00"^^xsd:dateTime  ;
             smart:hasUnixTimestamp "1606919400"^^xsd:integer  ;
.

ex:LK1E rdf:type smart:SmartLock ;
        saref:hasTimestamp "2020-12-02T14:30:00"^^xsd:dateTime  ;
        smart:hasUnixTimestamp "1606919400"^^xsd:integer  ;
        saref:hasState ex:CloseState ;
        smart:isLocatedIn ex:Entrance ;
.

#-----------

"""