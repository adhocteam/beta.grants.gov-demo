package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"html"
	"io"
	"io/ioutil"
	"log"
	"os"
	"time"
)

type Grants struct {
	XMLName                   xml.Name                      `xml:"Grants" json:"-"`
	OpportunitySynopsisDetail []OpportunitySynopsisDetail_1 `xml:"OpportunitySynopsisDetail_1_0" json:"OpportunitySynopsisDetail"`
	OpportunityForecastDetail []OpportunityForecastDetail_1 `xml:"OpportunityForecastDetail_1_0" json:"OpportunityForecastDetail"`
}

type OpportunitySynopsisDetail_1 struct {
	OpportunityID                      string
	OpportunityTitle                   string
	OpportunityNumber                  string
	OpportunityCategory                string
	OpportunityCategoryExplanation     string
	FundingInstrumentType              []string
	CategoryOfFundingActivity          []string
	CategoryExplanation                string
	CFDANumbers                        []string
	EligibleApplicants                 []string
	AdditionalInformationOnEligibility string
	AgencyCode                         string
	AgencyName                         string
	PostDate                           string
	CloseDate                          string
	CloseDateExplanation               string
	LastUpdatedDate                    string
	AwardCeiling                       string
	AwardFloor                         string
	EstimatedTotalProgramFunding       string
	ExpectedNumberOfAwards             string
	Description                        string
	Version                            string
	CostSharingOrMatchingRequirement   string
	ArchiveDate                        string
	AdditionalInformationURL           string
	AdditionalInformationText          string
	GrantorContactEmail                string
	GrantorContactEmailDescription     string
	GrantorContactText                 string
}

type OpportunityForecastDetail_1 struct {
	OpportunityID                         string
	OpportunityTitle                      string
	OpportunityNumber                     string
	OpportunityCategory                   string
	OpportunityCategoryExplanation        string
	FundingInstrumentType                 []string
	CategoryOfFundingActivity             []string
	CategoryExplanation                   string
	CFDANumbers                           []string
	EligibleApplicants                    []string
	AdditionalInformationOnEligibility    string
	AgencyCode                            string
	AgencyName                            string
	PostDate                              string
	LastUpdatedDate                       string
	EstimatedSynopsisPostDate             string
	FiscalYear                            string
	EstimatedSynopsisCloseDate            string
	EstimatedSynopsisCloseDateExplanation string
	EstimatedAwardDate                    string
	EstimatedProjectStartDate             string
	AwardCeiling                          string
	AwardFloor                            string
	EstimatedTotalProgramFunding          string
	ExpectedNumberOfAwards                string
	Description                           string
	Version                               string
	CostSharingOrMatchingRequirement      string
	ArchiveDate                           string
	AdditionalInformationURL              string
	AdditionalInformationText             string
	GrantorContactEmail                   string
	GrantorContactEmailDescription        string
	GrantorContactName                    string
	GrantorContactPhoneNumber             string
}

// toIsoDate converts string format from "MMDDYYYY" that appears in the
// Grants.gov XML to "YYYY-MM-DD"
func toIsoDate(dateStr string) string {
	if dateStr == "" {
		return ""
	}
	// Parse input date string using "01/02/2006" layout
	date, err := time.Parse("01022006", dateStr)
	if err != nil {
		log.Printf("[WARN] couldn't parse %q", dateStr)
		return ""
	}
	// Format date in "2006-01-02" layout
	return date.Format("2006-01-02")
}

func fixTypes(grants *Grants) {
	for i := range grants.OpportunitySynopsisDetail {
		opp := &grants.OpportunitySynopsisDetail[i]
		opp.PostDate = toIsoDate(opp.PostDate)
		opp.CloseDate = toIsoDate(opp.CloseDate)
		opp.LastUpdatedDate = toIsoDate(opp.LastUpdatedDate)
		opp.ArchiveDate = toIsoDate(opp.ArchiveDate)
	}

	for i := range grants.OpportunityForecastDetail {
		opp := &grants.OpportunityForecastDetail[i]
		opp.PostDate = toIsoDate(opp.PostDate)
		opp.LastUpdatedDate = toIsoDate(opp.LastUpdatedDate)
		opp.EstimatedSynopsisPostDate = toIsoDate(opp.EstimatedSynopsisPostDate)
		opp.EstimatedSynopsisCloseDate = toIsoDate(opp.EstimatedSynopsisCloseDate)
		opp.EstimatedAwardDate = toIsoDate(opp.EstimatedAwardDate)
		opp.EstimatedProjectStartDate = toIsoDate(opp.EstimatedProjectStartDate)
		opp.ArchiveDate = toIsoDate(opp.ArchiveDate)
	}
}

func fixEscaping(grants *Grants) {
	for i := range grants.OpportunitySynopsisDetail {
		opp := &grants.OpportunitySynopsisDetail[i]
		opp.OpportunityTitle = html.UnescapeString(opp.OpportunityTitle)
		opp.Description = html.UnescapeString(opp.Description)
	}

	for i := range grants.OpportunityForecastDetail {
		opp := &grants.OpportunityForecastDetail[i]
		opp.OpportunityTitle = html.UnescapeString(opp.OpportunityTitle)
		opp.Description = html.UnescapeString(opp.Description)
	}
}

func main() {
	var xmlFile io.Reader
	if len(os.Args) == 1 {
		xmlFile = os.Stdin
	} else {
		if f, err := os.Open(os.Args[1]); err != nil {
			log.Fatal(err)
		} else {
			defer f.Close()
			xmlFile = f
		}
	}

	xmlData, err := ioutil.ReadAll(xmlFile)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	var grants Grants
	err = xml.Unmarshal(xmlData, &grants)
	if err != nil {
		fmt.Println("Error unmarshalling XML:", err)
		return
	}

	fixTypes(&grants)
	fixEscaping(&grants)

	jsonData, err := json.MarshalIndent(grants, "", "    ")
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return
	}

	os.Stdout.Write(jsonData)
}
