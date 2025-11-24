from typing import Optional
from pydantic import BaseModel, Field, model_validator

def generate_income_statement_schema(fiscal_year: int):
    fy_label = str(fiscal_year)

    class IncomeStatement(BaseModel):

# =============================================================================
# NON-OPERATING: REALIZED INVESTMENT RESULTS
# =============================================================================

        non_op_realized_investment_net_with_donor_1: Optional[int] = Field(
            description=f"Non–operating REALIZED investment result WITH donor restrictions for {{fy_label}}. "
                        "Extract ONLY from the primary Statement of Activities/Operations table; "
                        "IGNORE Notes/MD&A/liquidity/supplementary schedules. "
                        "Use ONLY the current-year 'With Donor Restrictions' column (not prior years, not 'Total'). "
                        "Primary target row (case-insensitive; allow punctuation/spacing variants): "
                        "'Investment return above/(in deficit to) amounts designated for current operations'. "
                        "If that row exists, use it directly. "
                        "Otherwise, capture clearly labeled non-operating realized investment rows (same patterns as WITHOUT donor). "
                        "EXCLUDE unrealized amounts, combined realized+unrealized totals, operating investment income, appropriations, "
                        "grants, transfers, reclassifications, and non-investment items. "
                        "If both component lines and a realized-only non-operating subtotal exist, use the subtotal only. "
                        "Preserve sign (parentheses = negative). "
                        "Respect scale headings (e.g., 'in thousands'). "
                        "Extract the raw numeric value only."
        )

        non_op_realized_investment_net_with_donor_2: Optional[int] = Field(
            description=f"NON-OPERATING REALIZED investment result WITH donor restrictions for {fy_label}. "
                        "Definition: realized gains or losses from investment activities that are restricted by donors, "
                        "reported in the 'With Donor Restrictions' column of the primary Statement of Activities / Operations. "
                        "Represents the realized portion of total investment return related to restricted endowments, "
                        "excluding operating investment income and unrealized appreciation. "
                        "Typical labels include (case-insensitive): "
                        "  - 'Investment return above (in deficit to) amounts designated for current operations' "
                        "  - 'Non-operating realized investment return (with donor restrictions)' "
                        "  - 'Net realized gains (losses) — with donor restrictions' "
                        "  - 'Endowment return above spending distribution' "
                        "Primary extraction source: Statement of Activities / Operations, current-year 'With Donor Restrictions' column only. "
                        "IGNORE Notes, MD&A, liquidity disclosures, and supplementary schedules. "
                        "EXCLUDE unrealized gains/losses, combined realized+unrealized totals, operating investment income, appropriations, grants, or transfers. "
                        "If both component lines (realized gain and loss) and a subtotal exist, use the subtotal only. "
                        "When explicitly labeled totals exist (e.g., 'Total realized investment income (with donor restrictions)'), "
                        "prefer the subtotal rather than reconstructing it. "
                        "Maintain sign conventions (parentheses = negative) and respect scale indicators (e.g., 'in thousands'). "
                        "Return the raw numeric value only."
        )
        non_op_realized_investment_net_with_donor_3: Optional[int] = Field(
            description=f"NON-OPERATING REALIZED investment result WITH donor restrictions for {fy_label}. "
            "Definition: realized gains or losses from investment activities that are restricted by donors, "
            "reported exclusively in the 'With Donor Restrictions' column of the primary Statement of Activities / Operations. "
            "Represents the realized portion of total investment return related to restricted endowments, "
            "excluding unrealized appreciation and any operating investment income. "
            "Location restriction: extract ONLY from the NON-OPERATING section of the primary Statement of Activities / Operations, "
            "within the 'With Donor Restrictions' column. DO NOT extract from the operating section, summary totals, or footnotes. "
            "Common labels and variants include (case-insensitive): "
            "  - 'Non-operating realized investment return (with donor restrictions)' "
            "  - 'Net realized gains (losses) – with donor restrictions' "
            "  - 'Endowment return above spending distribution' "
            "  - 'Investment return above (in deficit to) amounts designated for current operations' "
            "  - 'Endowment investment return less amounts distributed for spending' "
            "  - 'Investment return – endowment distribution for spending' "
            "  - 'Investment income total (dividends & interest)' – only when clearly classified as non-operating "
            "Primary extraction source: Statement of Activities / Operations (non-operating part), 'With Donor Restrictions' column only. "
            "IGNORE Notes, MD&A, liquidity disclosures, and supplementary schedules. "
            "EXCLUDE unrealized gains/losses, combined realized+unrealized totals, operating investment income, appropriations, grants, or transfers. "
            "If both component lines (realized gain and loss) and a subtotal exist, use the subtotal only. "
            "When explicitly labeled totals exist (e.g., 'Total realized investment income (with donor restrictions)'), prefer the subtotal. "
            "Maintain sign conventions (parentheses = negative) and respect scale indicators (e.g., 'in thousands'). "
            "Return the raw numeric value only."
        )


        non_op_realized_investment_net_without_donor_1: Optional[int] = Field(
            description=f"NET REALIZED investment activity under the Non–Operating section for {{fy_label}} from the "
                        "current-year 'Without Donor Restrictions' column. "
                        "Extract ONLY from the primary Statement of Activities/Operations table. "
                        "Include ALL non-operating rows that clearly relate to realized investment results (preserve signs). "
                        "Preferred pattern: if a block titled 'Net Investment Appreciation Less Return' appears, compute "
                        "NET_REALIZED = 'Designated for Current Operations' + 'Allocation of Endowment Income to Operations'. "
                        "If separate realized gain and loss lines exist, sum them with signs. "
                        "If a clearly labeled realized-only non-operating subtotal exists, use that subtotal instead of components. "
                        "EXCLUDE unrealized amounts, combined realized+unrealized totals, operating investment income, appropriations, "
                        "grants, transfers, reclassifications, and non-investment items. "
                        "Label hints (case-insensitive): 'Investment', 'Realized', 'Net Realized Gains (Losses) — Nonoperating', "
                        "'Net Investment Appreciation Less Return', 'Designated for Current Operations', "
                        "'Allocation of Endowment Income to Operations'. "
                        "Preserve sign (parentheses = negative). "
                        "Respect scale headings (e.g., 'in thousands'). "
                        "Extract the raw numeric value only."
        )

        non_op_realized_investment_net_without_donor_2: Optional[int] = Field(
            description=f"NET REALIZED non-operating investment activity WITHOUT donor restrictions (WDR) for {fy_label}. "
                        "Definition: realized investment income, gains, or losses that occur in the non-operating section of the Statement of Activities, "
                        "excluding the portion appropriated for operations. "
                        "Reflects the realized component of total investment return for the unrestricted portion of the endowment and other investment pools. "
                        "Primary source: current-year 'Without Donor Restrictions' column of the Statement of Activities / Operations table. "
                        "Include all clearly labeled non-operating realized investment lines (e.g., 'Realized investment gain/loss — non-operating', "
                        "'Net realized gains (losses) — Without donor restrictions'). "
                        "Preferred extraction pattern: if a subtotal block titled 'Net Investment Appreciation Less Return' or similar appears, compute: "
                        "  NET_REALIZED = 'Designated for Current Operations' + 'Allocation of Endowment Income to Operations' (if both present). "
                        "Related terminology: 'Investment return', 'Endowment distribution', 'Amounts distributed for spending', 'Other investment income'. "
                        "Conceptually, total investment income equals: "
                        "  (Endowment investment return + Other investment income), "
                        "and the operating portion equals: "
                        "  (Endowment distribution to operations + Other investment income (operating)). "
                        "Thus, the non-operating realized component may be derived as: "
                        "  (Total WDR investment return − Endowment distribution for spending), "
                        "when explicit non-operating lines are missing but component structure is evident. "
                        "EXCLUDE unrealized changes, reclassifications, transfers, and operating amounts. "
                        "If separate realized gain and realized loss lines exist, sum with proper signs. "
                        "Use subtotal if clearly labeled 'realized only'. "
                        "Maintain sign conventions (parentheses = negative) and respect scale headings. "
                        "Return the raw numeric value only."
        )

        non_op_realized_investment_net_without_donor_3: Optional[int] = Field(
            description=f"NET realized investment activity under the Non–Operating section for {{fy_label}} from the "
                        "current-year 'Without Donor Restrictions' column. "
                        "Extract ONLY from the primary Statement of Activities/Operations table. "
                        "Include ALL non-operating rows that clearly relate to realized investment results (preserve signs). "
                        "Preferred pattern: if a block titled 'Net Investment Appreciation Less Return' appears, compute "
                        "NET_REALIZED = 'Designated for Current Operations' + 'Allocation of Endowment Income to Operations'. "
                        "If separate realized gain and loss lines exist, sum them with signs. " # just grab the number, do not care the gain/loss !!!
                        "If a clearly labeled realized-only non-operating subtotal exists, use that subtotal instead of components. "
                        "EXCLUDE unrealized amounts, combined realized+unrealized totals, operating investment income, appropriations, "
                        "grants, transfers, reclassifications, and non-investment items. "
                        "Label hints (case-insensitive): 'Investment', 'Realized', 'Net Realized Gains (Losses) — Nonoperating', "
                        "'Net Investment Appreciation Less Return', 'Designated for Current Operations', "
                        "'Allocation of Endowment Income to Operations'. "
                        "Preserve sign (parentheses = negative). "
                        "Respect scale headings (e.g., 'in thousands'). "
                        "Extract the raw numeric value only."
        )
        non_op_realized_investment_net_without_donor_4: Optional[int] = Field(
            description=f"NET REALIZED non-operating investment activity WITHOUT donor restrictions for {fy_label}. "
            "Definition: realized gains or losses from investment activities not subject to donor-imposed restrictions, "
            "reported exclusively in the 'Without Donor Restrictions' column of the primary Statement of Activities / Operations. "
            "Includes all realized investment return components classified as non-operating (exclude operating investment income). "
            "Location restriction: extract ONLY from the NON-OPERATING section of the primary Statement of Activities / Operations, "
            "within the 'Without Donor Restrictions' column. DO NOT extract from the operating section, subtotal summaries, or footnotes. "
            "Preferred extraction source: primary Statement of Activities / Operations table, non-operating part. "
            "Common labels and variants (case-insensitive) include: "
            "  - 'Net investment appreciation (less) return' "
            "  - 'Investment return designated for current operations' (exclude if labeled operating) "
            "  - 'Allocation of endowment income to operations' (exclude if under operating) "
            "  - 'Net realized gains (losses) – nonoperating' "
            "  - 'Endowment investment return above spending distribution' "
            "  - 'Investment income total (dividends & interest)' – only when clearly marked non-operating "
            "  - 'Net investment gain and amounts distributed for spending' (if subtotal shown in non-operating section) "
            "EXCLUDE unrealized amounts, combined realized+unrealized totals, grants, transfers, reclassifications, or non-investment income. "
            "Preserve sign (parentheses = negative) and respect unit scale (e.g., 'in thousands'). "
            "Extract the raw numeric value only."
        )

 
    @model_validator(mode="after")
    def validate_consistency(self):
        """Validate logical consistency between related fields with detailed warnings"""
        tolerance = 1000  # Allow $1,000 tolerance for rounding differences

        # Check tuition consistency
        if (self.gross_tuition_revenue is not None and 
            self.financial_aid is not None and 
            self.net_tuition_revenue is not None):
            expected_net = self.gross_tuition_revenue - self.financial_aid
            if abs(expected_net - self.net_tuition_revenue) > tolerance:
                print(f"⚠️  TUITION INCONSISTENCY:")
                print(f"   Expected Net Tuition: ${expected_net:,} (Gross ${self.gross_tuition_revenue:,} - Aid ${self.financial_aid:,})")
                print(f"   Actual Net Tuition: ${self.net_tuition_revenue:,}")
                print(f"   Difference: ${abs(expected_net - self.net_tuition_revenue):,}")

        # Check government grants total consistency
        if (self.government_grants_contracts_total is not None and 
            self.federal_grants_contracts is not None and 
            self.state_local_grants_contracts is not None):
            expected_total = self.federal_grants_contracts + self.state_local_grants_contracts
            if abs(expected_total - self.government_grants_contracts_total) > tolerance:
                print(f"⚠️  GOVERNMENT GRANTS INCONSISTENCY:")
                print(f"   Expected Total: ${expected_total:,} (Federal ${self.federal_grants_contracts:,} + State/Local ${self.state_local_grants_contracts:,})")
                print(f"   Actual Total: ${self.government_grants_contracts_total:,}")
                print(f"   Difference: ${abs(expected_total - self.government_grants_contracts_total):,}")

        # Check total gifts consistency
        if (self.government_grants_contracts_total is not None and 
            self.state_appropriations is not None and 
            self.private_gifts_grants_contracts is not None and 
            self.total_gifts_contracts_other_support is not None):
            expected_total = (self.government_grants_contracts_total + 
                            self.state_appropriations + 
                            self.private_gifts_grants_contracts)
            if abs(expected_total - self.total_gifts_contracts_other_support) > tolerance:
                print(f"⚠️  TOTAL GIFTS/GRANTS INCONSISTENCY:")
                print(f"   Expected Total: ${expected_total:,}")
                print(f"   - Government Grants: ${self.government_grants_contracts_total:,}")
                print(f"   - State Appropriations: ${self.state_appropriations:,}")
                print(f"   - Private Gifts: ${self.private_gifts_grants_contracts:,}")
                print(f"   Actual Total: ${self.total_gifts_contracts_other_support:,}")
                print(f"   Difference: ${abs(expected_total - self.total_gifts_contracts_other_support):,}")

        # Check operating income consistency
        if (self.total_operating_revenue is not None and 
            self.total_operating_expense is not None and 
            self.net_operating_income is not None):
            expected_income = self.total_operating_revenue - self.total_operating_expense
            if abs(expected_income - self.net_operating_income) > tolerance:
                print(f"⚠️  OPERATING INCOME INCONSISTENCY:")
                print(f"   Expected Income: ${expected_income:,} (Revenue ${self.total_operating_revenue:,} - Expenses ${self.total_operating_expense:,})")
                print(f"   Actual Income: ${self.net_operating_income:,}")
                print(f"   Difference: ${abs(expected_income - self.net_operating_income):,}")

        # Check instruction and research consistency
        if (self.instructional_expense is not None and 
            self.research_expense is not None and 
            self.instructional_research_expense is not None):
            expected_combined = self.instructional_expense + self.research_expense
            if abs(expected_combined - self.instructional_research_expense) > tolerance:
                print(f"⚠️  INSTRUCTION + RESEARCH INCONSISTENCY:")
                print(f"   Expected Combined: ${expected_combined:,} (Instruction ${self.instructional_expense:,} + Research ${self.research_expense:,})")
                print(f"   Actual Combined: ${self.instructional_research_expense:,}")
                print(f"   Difference: ${abs(expected_combined - self.instructional_research_expense):,}")

        # Check total net assets change consistency
        if (self.change_net_assets_without_donor_restrictions is not None and 
            self.change_net_assets_with_donor_restrictions is not None and 
            self.total_change_in_net_assets is not None):
            expected_total = (self.change_net_assets_without_donor_restrictions + 
                            self.change_net_assets_with_donor_restrictions)
            if abs(expected_total - self.total_change_in_net_assets) > tolerance:
                print(f"⚠️  NET ASSETS CHANGE INCONSISTENCY:")
                print(f"   Expected Total: ${expected_total:,}")
                print(f"   - Without Restrictions: ${self.change_net_assets_without_donor_restrictions:,}")
                print(f"   - With Restrictions: ${self.change_net_assets_with_donor_restrictions:,}")
                print(f"   Actual Total: ${self.total_change_in_net_assets:,}")
                print(f"   Difference: ${abs(expected_total - self.total_change_in_net_assets):,}")

        # Check investment income consistency if both operating and total are available
        if (self.investment_income_total is not None and 
            self.investment_income_operations is not None):
            non_operating_amount = self.investment_income_total - self.investment_income_operations
            if abs(non_operating_amount) > tolerance:
                if non_operating_amount > 0:
                    print(f"ℹ️  INVESTMENT INCOME ALLOCATION:")
                    print(f"   Total Investment Income: ${self.investment_income_total:,}")
                    print(f"   Operating Portion: ${self.investment_income_operations:,}")
                    print(f"   Non-Operating Portion: ${non_operating_amount:,}")
                else:
                    print(f"⚠️  UNUSUAL INVESTMENT ALLOCATION:")
                    print(f"   Operating investment income (${self.investment_income_operations:,}) exceeds total (${self.investment_income_total:,})")

        return self
    # @model_validator(mode="after")
    # def compute_derived_fields(self):
    #     """Compute derived fields and validate relationships"""
        
    #     # Calculate tuition relationships - force gross calculation if both net and aid are available
    #     if (self.net_tuition_revenue is not None and 
    #         self.financial_aid is not None and
    #         self.gross_tuition_revenue is None):
    #         self.gross_tuition_revenue = self.net_tuition_revenue + self.financial_aid
        
    #     # Calculate government support total if components exist but total doesn't
    #     if (self.federal_grants_contracts is not None and 
    #         self.state_local_grants_contracts is not None and 
    #         self.government_grants_contracts_total is None):
    #         self.government_grants_contracts_total = (
    #             self.federal_grants_contracts + self.state_local_grants_contracts
    #         )
        
    #     # Calculate total gifts if all components exist but total doesn't
    #     if (self.government_grants_contracts_total is not None and 
    #         self.state_appropriations is not None and 
    #         self.private_gifts_grants_contracts is not None and 
    #         self.total_gifts_contracts_other_support is None):
    #         self.total_gifts_contracts_other_support = (
    #             self.government_grants_contracts_total + 
    #             self.state_appropriations + 
    #             self.private_gifts_grants_contracts
    #         )
        
    #     # Calculate net operating income if components exist but total doesn't
    #     if (self.total_operating_revenue is not None and 
    #         self.total_operating_expense is not None and 
    #         self.net_operating_income is None):
    #         self.net_operating_income = (
    #             self.total_operating_revenue - self.total_operating_expense
    #         )
        
    #     # Calculate total net assets change if components exist but total doesn't
    #     if (self.change_net_assets_without_donor_restrictions is not None and 
    #         self.change_net_assets_with_donor_restrictions is not None and 
    #         self.total_change_in_net_assets is None):
    #         self.total_change_in_net_assets = (
    #             self.change_net_assets_without_donor_restrictions + 
    #             self.change_net_assets_with_donor_restrictions
    #         )
        
    #     # Calculate combined instruction and research if separate values exist but combined doesn't
    #     if (self.instructional_expense is not None and 
    #         self.research_expense is not None and 
    #         self.instructional_research_expense is None):
    #         self.instructional_research_expense = (
    #             self.instructional_expense + self.research_expense
    #         )
        
    #     return self

    # @model_validator(mode="after")
    # def validate_consistency(self):
    #     """Validate logical consistency between related fields with detailed warnings"""
        
    #     tolerance = 1000  # Allow $1,000 tolerance for rounding differences
        
    #     # Check tuition consistency
    #     if all(x is not None for x in [self.gross_tuition_revenue, self.financial_aid, self.net_tuition_revenue]):
    #         expected_net = self.gross_tuition_revenue - self.financial_aid
    #         if abs(expected_net - self.net_tuition_revenue) > tolerance:
    #             print(f"⚠️  TUITION INCONSISTENCY:")
    #             print(f"   Expected Net Tuition: ${expected_net:,} (Gross ${self.gross_tuition_revenue:,} - Aid ${self.financial_aid:,})")
    #             print(f"   Actual Net Tuition: ${self.net_tuition_revenue:,}")
    #             print(f"   Difference: ${abs(expected_net - self.net_tuition_revenue):,}")
        
    #     # Check government grants total consistency
    #     if (self.government_grants_contracts_total is not None and 
    #         self.federal_grants_contracts is not None and 
    #         self.state_local_grants_contracts is not None):
    #         expected_total = self.federal_grants_contracts + self.state_local_grants_contracts
    #         if abs(expected_total - self.government_grants_contracts_total) > tolerance:
    #             print(f"⚠️  GOVERNMENT GRANTS INCONSISTENCY:")
    #             print(f"   Expected Total: ${expected_total:,} (Federal ${self.federal_grants_contracts:,} + State/Local ${self.state_local_grants_contracts:,})")
    #             print(f"   Actual Total: ${self.government_grants_contracts_total:,}")
    #             print(f"   Difference: ${abs(expected_total - self.government_grants_contracts_total):,}")
        
    #     # Check total gifts consistency
    #     if all(x is not None for x in [self.government_grants_contracts_total, self.state_appropriations, 
    #                                 self.private_gifts_grants_contracts, self.total_gifts_contracts_other_support]):
    #         expected_total = (self.government_grants_contracts_total + 
    #                         self.state_appropriations + 
    #                         self.private_gifts_grants_contracts)
    #         if abs(expected_total - self.total_gifts_contracts_other_support) > tolerance:
    #             print(f"⚠️  TOTAL GIFTS/GRANTS INCONSISTENCY:")
    #             print(f"   Expected Total: ${expected_total:,}")
    #             print(f"   - Government Grants: ${self.government_grants_contracts_total:,}")
    #             print(f"   - State Appropriations: ${self.state_appropriations:,}")
    #             print(f"   - Private Gifts: ${self.private_gifts_grants_contracts:,}")
    #             print(f"   Actual Total: ${self.total_gifts_contracts_other_support:,}")
    #             print(f"   Difference: ${abs(expected_total - self.total_gifts_contracts_other_support):,}")
        
    #     # Check operating income consistency
    #     if all(x is not None for x in [self.total_operating_revenue, self.total_operating_expense, self.net_operating_income]):
    #         expected_income = self.total_operating_revenue - self.total_operating_expense
    #         if abs(expected_income - self.net_operating_income) > tolerance:
    #             print(f"⚠️  OPERATING INCOME INCONSISTENCY:")
    #             print(f"   Expected Income: ${expected_income:,} (Revenue ${self.total_operating_revenue:,} - Expenses ${self.total_operating_expense:,})")
    #             print(f"   Actual Income: ${self.net_operating_income:,}")
    #             print(f"   Difference: ${abs(expected_income - self.net_operating_income):,}")
        
    #     # Check instruction and research consistency
    #     if all(x is not None for x in [self.instructional_expense, self.research_expense, self.instructional_research_expense]):
    #         expected_combined = self.instructional_expense + self.research_expense
    #         if abs(expected_combined - self.instructional_research_expense) > tolerance:
    #             print(f"⚠️  INSTRUCTION + RESEARCH INCONSISTENCY:")
    #             print(f"   Expected Combined: ${expected_combined:,} (Instruction ${self.instructional_expense:,} + Research ${self.research_expense:,})")
    #             print(f"   Actual Combined: ${self.instructional_research_expense:,}")
    #             print(f"   Difference: ${abs(expected_combined - self.instructional_research_expense):,}")
        
    #     # Check total net assets change consistency
    #     if all(x is not None for x in [self.change_net_assets_without_donor_restrictions, 
    #                                 self.change_net_assets_with_donor_restrictions, 
    #                                 self.total_change_in_net_assets]):
    #         expected_total = (self.change_net_assets_without_donor_restrictions + 
    #                         self.change_net_assets_with_donor_restrictions)
    #         if abs(expected_total - self.total_change_in_net_assets) > tolerance:
    #             print(f"⚠️  NET ASSETS CHANGE INCONSISTENCY:")
    #             print(f"   Expected Total: ${expected_total:,}")
    #             print(f"   - Without Restrictions: ${self.change_net_assets_without_donor_restrictions:,}")
    #             print(f"   - With Restrictions: ${self.change_net_assets_with_donor_restrictions:,}")
    #             print(f"   Actual Total: ${self.total_change_in_net_assets:,}")
    #             print(f"   Difference: ${abs(expected_total - self.total_change_in_net_assets):,}")
        
    #     # Check investment income consistency if both operating and total are available
    #     if (self.investment_income_total is not None and 
    #         self.investment_income_operations is not None):
    #         non_operating_amount = self.investment_income_total - self.investment_income_operations
    #         if abs(non_operating_amount) > tolerance:
    #             if non_operating_amount > 0:
    #                 print(f"ℹ️  INVESTMENT INCOME ALLOCATION:")
    #                 print(f"   Total Investment Income: ${self.investment_income_total:,}")
    #                 print(f"   Operating Portion: ${self.investment_income_operations:,}")
    #                 print(f"   Non-Operating Portion: ${non_operating_amount:,}")
    #             else:
    #                 print(f"⚠️  UNUSUAL INVESTMENT ALLOCATION:")
    #                 print(f"   Operating investment income (${self.investment_income_operations:,}) exceeds total (${self.investment_income_total:,})")
        
    #     return self

    return IncomeStatement