natural_restricted_sentences = [
    # Basic sentences
    "if condition_a then condition_b",
    "condition_a and condition_b",
    "not condition_c",
    "(condition_a and (condition_b or condition_c))",
    "not (condition_a and condition_b)",
    "(not condition_a) or (condition_b and condition_c)",
    "if (condition_a and condition_b) then (condition_c or not condition_d)",
    
    # Deeper nesting
    "not (condition_a and (condition_b or (condition_c and condition_d)))",
    "((not condition_a) and condition_b) or (condition_c and (not condition_d))",
    "if ((condition_a or condition_b) and (not condition_c)) then (condition_d or not condition_e)",
    
    # Multiple levels of implication
    "if (if condition_a then condition_b) then (if condition_b then condition_c)",
    "not (if (condition_a and condition_b) then (condition_c or condition_d))",
    "if (not condition_a) then (not (condition_b or condition_c))",
    
    # Combining multiple operators
    "(condition_a or (condition_b and (if condition_c then condition_d)))",
    "not ((if condition_a then condition_b) or (condition_c and not condition_d))",
    "(if (condition_a and condition_b) then condition_c) or (not condition_d)",
    
    # Extreme nesting
    "not (if (condition_a and (condition_b or condition_b)) then ((condition_c and condition_d) → (not condition_e)))",
    
    "(((if condition_a then condition_b) → condition_c) and condition_d) or (not (condition_e and condition_f))",
    
    # Moderately Nested Sentences
    "if (condition_a and condition_b) then (condition_c or condition_d)",
    "not (condition_a and (condition_b or condition_c))",
    "(condition_a or (condition_b and condition_c))",
    "if ((condition_a or condition_b) and condition_c) then condition_d",
    "not ((condition_a and condition_b) or (if condition_c then condition_d))",
    
    # Deeply Nested Sentences
    "if (if condition_a then condition_b) then condition_c",
    "if (if condition_a then condition_b) then ((if condition_b then condition_c) → condition_d)",
    "not (if ((condition_a and condition_b) → condition_c) then (condition_d or condition_e))",
    "(((if condition_a then condition_b) → condition_c) and condition_d) or (not condition_e)",
    "(not (condition_a and condition_b)) or ((if condition_c then condition_d) and condition_e)",
    
    # Complex Logical Operations
    "if ((condition_a or condition_b) and (if condition_c then condition_d)) then (condition_e and condition_f)",
    "not (((condition_a and condition_b) → condition_c) or (condition_d and condition_e))",
    "(if (if condition_a then condition_b) then condition_c) or (not condition_d)",
    "if (((condition_a and (condition_b or condition_c)) → condition_d)) then condition_e",
    "not ((condition_a and condition_b) → (condition_c and (condition_d or condition_e)))",
]

natural_restricted_sentences_auth_context = [
    # Basic sentences
    "if user_is_authenticated then user_has_permission",
    "user_is_authenticated and user_has_permission",
    "not data_is_invalid",
    "(user_is_authenticated and (user_has_permission or data_is_valid))",
    "not (user_is_authenticated and user_has_permission)",
    "(not user_is_authenticated) or (user_has_permission and data_is_valid)",
    "if (user_is_authenticated and user_has_permission) then (data_is_valid or not process_can_continue)",
    
    # Deeper nesting
    "not (user_is_authenticated and (user_has_permission or (data_is_valid and process_can_continue)))",
    "((not user_is_authenticated) and user_has_permission) or (data_is_valid and (not process_can_continue))",
    "if ((user_is_authenticated or user_has_permission) and (not data_is_invalid)) then (process_can_continue or not system_is_operational)",
    
    # Multiple levels of implication
    "if (if user_is_authenticated then user_has_permission) then (if user_has_permission then data_is_valid)",
    "not (if (user_is_authenticated and user_has_permission) then (data_is_valid or process_can_continue))",
    "if (not user_is_authenticated) then (not (user_has_permission or data_is_valid))",
    
    # Combining multiple operators
    "(user_is_authenticated or (user_has_permission and (if data_is_valid then process_can_continue)))",
    "not ((if user_is_authenticated then user_has_permission) or (data_is_valid and not process_can_continue))",
    "(if (user_is_authenticated and user_has_permission) then data_is_valid) or (not process_can_continue)",
    
    # Extreme nesting
    "not (if (user_is_authenticated and (user_has_permission or user_has_permission)) then ((data_is_valid and process_can_continue) → (not system_is_operational)))",
    "(((if user_is_authenticated then user_has_permission) → data_is_valid) and process_can_continue) or (not (system_is_operational and log_is_enabled))",
    
    # Moderately Nested Sentences
    "if (user_is_authenticated and user_has_permission) then (data_is_valid or process_can_continue)",
    "not (user_is_authenticated and (user_has_permission or data_is_valid))",
    "(user_is_authenticated or (user_has_permission and data_is_valid))",
    "if ((user_is_authenticated or user_has_permission) and data_is_valid) then process_can_continue",
    "not ((user_is_authenticated and user_has_permission) or (if data_is_valid then process_can_continue))",
    
    # Deeply Nested Sentences
    "if (if user_is_authenticated then user_has_permission) then data_is_valid",
    "if (if user_is_authenticated then user_has_permission) then ((if user_has_permission then data_is_valid) → process_can_continue)",
    "not (if ((user_is_authenticated and user_has_permission) → data_is_valid) then (process_can_continue or system_is_operational))",
    "(((if user_is_authenticated then user_has_permission) → data_is_valid) and process_can_continue) or (not system_is_operational)",
    "(not (user_is_authenticated and user_has_permission)) or ((if data_is_valid then process_can_continue) and system_is_operational)",
    
    # Complex Logical Operations
    "if ((user_is_authenticated or user_has_permission) and (if data_is_valid then process_can_continue)) then (system_is_operational and log_is_enabled)",
    "not (((user_is_authenticated and user_has_permission) → data_is_valid) or (process_can_continue and system_is_operational))",
    "(if (if user_is_authenticated then user_has_permission) then data_is_valid) or (not process_can_continue)",
    "if (((user_is_authenticated and (user_has_permission or data_is_valid)) → process_can_continue)) then system_is_operational",
    "not ((user_is_authenticated and user_has_permission) → (data_is_valid and (process_can_continue or system_is_operational)))",
]

cute_natural_restricted_sentences = [
    # Basic sentences
    "if acaba_de_llover then el_suelo_esta_mojado",
    "has_pizza and owns_a_unicorn",
    "not is_sleeping",
    "(has_pizza and (owns_a_unicorn or is_sleeping))",
    "not (has_pizza and owns_a_unicorn)",
    "(not has_pizza) or (owns_a_unicorn and is_sleeping)",
    "if (has_pizza and owns_a_unicorn) then (is_sleeping or not has_dancing_shoes)",
    
    # Deeper nesting
    "not (has_pizza and (owns_a_unicorn or (is_sleeping and has_dancing_shoes)))",
    "((not has_pizza) and owns_a_unicorn) or (is_sleeping and (not has_dancing_shoes))",
    "if ((has_pizza or owns_a_unicorn) and (not is_sleeping)) then (has_dancing_shoes or not can_speak_morse_code)",
    
    # Multiple levels of implication
    "if (if has_pizza then owns_a_unicorn) then (if owns_a_unicorn then is_sleeping)",
    "not (if (has_pizza and owns_a_unicorn) then (is_sleeping or has_dancing_shoes))",
    "if (not has_pizza) then (not (owns_a_unicorn or is_sleeping))",
    
    # Combining multiple operators
    "(has_pizza or (owns_a_unicorn and (if is_sleeping then has_dancing_shoes)))",
    "not ((if has_pizza then owns_a_unicorn) or (is_sleeping and not has_dancing_shoes))",
    "(if (has_pizza and owns_a_unicorn) then is_sleeping) or (not has_dancing_shoes)",
    
    # Extreme nesting
    "not (if (has_pizza and (owns_a_unicorn or owns_a_unicorn)) then ((is_sleeping and has_dancing_shoes) → (not can_speak_morse_code)))",
    "(((if has_pizza then owns_a_unicorn) → is_sleeping) and has_dancing_shoes) or (not (can_speak_morse_code and has_flying_cats))",
    
    # Moderately Nested Sentences
    "if (has_pizza and owns_a_unicorn) then (is_sleeping or has_dancing_shoes)",
    "not (has_pizza and (owns_a_unicorn or is_sleeping))",
    "(has_pizza or (owns_a_unicorn and is_sleeping))",
    "if ((has_pizza or owns_a_unicorn) and is_sleeping) then has_dancing_shoes",
    "not ((has_pizza and owns_a_unicorn) or (if is_sleeping then has_dancing_shoes))",
    
    # Deeply Nested Sentences
    "if (if has_pizza then owns_a_unicorn) then is_sleeping",
    "if (if has_pizza then owns_a_unicorn) then ((if owns_a_unicorn then is_sleeping) → has_dancing_shoes)",
    "not (if ((has_pizza and owns_a_unicorn) → is_sleeping) then (has_dancing_shoes or can_speak_morse_code))",
    "(((if has_pizza then owns_a_unicorn) → is_sleeping) and has_dancing_shoes) or (not can_speak_morse_code)",
    "(not (has_pizza and owns_a_unicorn)) or ((if is_sleeping then has_dancing_shoes) and can_speak_morse_code)",
    
    # Complex Logical Operations
    "if ((has_pizza or owns_a_unicorn) and (if is_sleeping then has_dancing_shoes)) then (can_speak_morse_code and has_flying_cats)",
    "not (((has_pizza and owns_a_unicorn) → is_sleeping) or (has_dancing_shoes and can_speak_morse_code))",
    "(if (if has_pizza then owns_a_unicorn) then is_sleeping) or (not has_dancing_shoes)",
    "if (((has_pizza and (owns_a_unicorn or is_sleeping)) → has_dancing_shoes)) then can_speak_morse_code",
    "not ((has_pizza and owns_a_unicorn) → (is_sleeping and (has_dancing_shoes or can_speak_morse_code)))",
]

natural_restricted_sentences_serious = [
    # Basic sentences
    "if is_fire_detected then activate_fire_alarm",
    "is_door_locked and is_security_system_armed",
    "not is_authorized_user",
    "(is_emergency and (is_medical_staff_on_duty or is_ambulance_available))",
    "not (is_patient_stable and is_transportation_ready)",
    "(not is_building_evacuated) or (is_emergency_responders_arrived and is_emergency_under_control)",
    "if (is_fire_detected and is_sprinkler_system_active) then (is_fire_alarm_active or not is_emergency_call_made)",
    
    # Deeper nesting
    "not (is_server_operational and (is_backup_in_progress or (is_critical_data_accessed and is_network_stable)))",
    "((not is_security_alert_raised) and is_security_cameras_active) or (is_emergency_exit_accessible and (not is_fire_alarm_triggered))",
    "if ((is_system_overheating or is_critical_service_down) and (not is_admin_notified)) then (is_maintenance_crew_alerted or not is_redundancy_active)",
    
    # Multiple levels of implication
    "if (if is_access_granted then is_room_unlocked) then (if is_room_unlocked then is_motion_detected)",
    "not (if (is_fire_alarm_silenced and is_emergency_reported) then (is_fire_drill_in_progress or is_emergency_resolved))",
    "if (not is_user_authenticated) then (not (is_access_granted or is_admin_notified))",
    
    # Combining multiple operators
    "(is_user_logged_in or (is_admin_privileges_required and (if is_two_factor_enabled then is_user_verified)))",
    "not ((if is_data_encrypted then is_backup_secure) or (is_data_access_allowed and not is_admin_override_used))",
    "(if (is_security_protocol_active and is_access_granted) then is_system_log_updated) or (not is_system_compromised)",
    
    # Extreme nesting
    "not (if (is_fire_detected and (is_sprinkler_active or is_sprinkler_active)) then ((is_emergency_exit_unobstructed and is_alarm_triggered) → (not is_fire_contained)))",
    
    "(((if is_network_accessed then is_traffic_monitored) → is_threat_detected) and is_intrusion_prevention_active) or (not (is_threat_logged and is_admin_notified))",
    
    # Moderately Nested Sentences
    "if (is_patient_monitored and is_vital_signs_stable) then (is_doctor_notified or is_treatment_initiated)",
    "not (is_data_integrity_verified and (is_backup_in_progress or is_data_access_requested))",
    "(is_security_protocol_active or (is_access_attempted and is_monitoring_enabled))",
    "if ((is_alarm_triggered or is_emergency_alert_issued) and is_response_team_alerted) then is_emergency_under_control",
    "not ((is_power_on and is_backup_power_available) or (if is_critical_system_active then is_system_stable))",
    
    # Deeply Nested Sentences
    "if (if is_fire_detected then is_alarm_active) then is_sprinkler_system_active",
    "if (if is_user_authenticated then is_access_granted) then ((if is_access_granted then is_security_log_updated) → is_system_stable)",
    "not (if ((is_fire_alarm_active and is_fire_suppressed) → is_emergency_resolved) then (is_emergency_reported or is_false_alarm_flagged))",
    "(((if is_emergency_protocol_active then is_casualty_reported) → is_response_team_alerted) and is_evacuation_ordered) or (not is_alarm_resolved)",
    "(not (is_network_secure and is_threat_detected)) or ((if is_intrusion_detected then is_threat_neutralized) and is_log_updated)",
    
    # Complex Logical Operations
    "if ((is_server_overloaded or is_network_slow) and (if is_maintenance_window_active then is_server_rebooted)) then (is_downtime_minimized and is_performance_improved)",
    "not (((is_hardware_fault_detected and is_system_reboot_initiated) → is_issue_resolved) or (is_system_logs_available and is_maintenance_team_notified))",
    "(if (if is_breach_detected then is_admin_notified) then is_incident_logged) or (not is_system_compromised)",
    "if (((is_fire_alarm_active and (is_evacuated or is_emergency_services_called)) → is_emergency_resolved)) then is_situation_stabilized",
    "not ((is_power_failure_detected and is_backup_power_available) → (is_system_shutdown and (is_admin_alerted or is_service_resumed)))",
]

natural_restricted_sentences_debate = [
    # Basic sentences
    "if free_will_exists then determinism_is_false",
    "consciousness_is_fundamental and materialism_is_incomplete",
    "not morality_is_absolute",
    "(universe_is_finite and (time_is_cyclic or reality_is_simulation))",
    "not (ai_can_experience_emotions and ai_can_have_rights)",
    "(not multiverse_exists) or (quantum_entanglement_explains_free_will and objective_reality_is_illusory)",
    "if (ethics_are_relative and moral_realism_is_false) then (societal_progress_is_meaningless or not altruism_is_rational)",
    
    # Deeper nesting
    "not (human_cognition_is_limited and (philosophy_can_prove_truth or (science_can_explain_existence and religion_is_valid)))",
    "((not free_markets_are_optimal) and socialism_is_practical) or (capitalism_is_sustainable and (not democracy_is_perfect))",
    "if ((infinity_is_real or numbers_are_inventions) and (not mathematics_describes_reality)) then (the_universe_is_ordered or not chaos_is_fundamental)",
    
    # Multiple levels of implication
    "if (if morality_is_subjective then universal_ethics_are_impossible) then (if universal_ethics_are_impossible then global_cooperation_is_unachievable)",
    "not (if (consciousness_is_a_computation and humans_are_machines) then (free_will_is_an_illusion or identity_is_illusory))",
    "if (not the_universe_has_a_purpose) then (not (life_has_intrinsic_meaning or nihilism_is_correct))",
    
    # Combining multiple operators
    "(truth_is_objective or (knowledge_is_contextual and (if reality_is_objective then human_perception_is_flawed)))",
    "not ((if technology_can_solve_ethics then humanity_will_transcend) or (artificial_superintelligence_is_safe and not posthumanism_is_inevitable))",
    "(if (existence_is_pain and suffering_is_unavoidable) then morality_is_pointless) or (not utilitarianism_is_correct)",
    
    # Extreme nesting
    "not (if (the_universe_is_finite and (time_is_discrete or time_is_continuous)) then ((consciousness_is_immaterial and morality_is_universal) → (not free_will_is_real)))",
    
    "(((if god_exists then evil_is_unexplainable) → morality_is_subjective) and reality_is_incomprehensible) or (not (truth_is_knowable and logic_is_consistent))",
    
    # Moderately Nested Sentences
    "if (humans_are_biological_machines and consciousness_emerges_from_matter) then (identity_is_an_illusion or self_awareness_is_a_fluke)",
    "not (reality_is_simulation and (existence_is_illusory or reality_is_objective))",
    "(free_will_exists or (determinism_is_true and consciousness_is_illusionary))",
    "if ((knowledge_is_power or truth_is_subjective) and morality_is_cultural) then progress_is_relative",
    "not ((reality_is_an_emergent_property and truth_is_flexible) or (if morality_is_situational then ethics_are_mutable))",
    
    # Deeply Nested Sentences
    "if (if consciousness_is_quantum then free_will_is_possible) then identity_is_non_material",
    "if (if humanity_is_insignificant then meaning_is_relative) then ((if meaning_is_relative then progress_is_arbitrary) → cooperation_is_futile)",
    "not (if ((truth_is_discovered and reality_is_objective) → free_will_is_real) then (morality_is_illusion or truth_is_relative))",
    "(((if morality_is_evolved then altruism_is_genetic) → ethics_are_adaptive) and progress_is_evolutionary) or (not truth_is_constant)",
    "(not (universe_is_ordered and chaos_is_an_illusion)) or ((if ethics_are_flexible then morality_is_adaptive) and truth_is_malleable)",
    
    # Complex Logical Operations
    "if ((science_can_explain_existence or religion_is_valid) and (if philosophy_is_valid then knowledge_is_limitless)) then (truth_is_subjective and morality_is_adaptive)",
    "not (((truth_is_discovered and reality_is_objective) → meaning_is_relative) or (ethics_are_contextual and progress_is_subjective))",
    "(if (if god_does_not_exist then morality_is_arbitrary) then free_will_is_an_illusion) or (not truth_is_universal)",
    "if (((the_universe_is_a_hologram and (consciousness_is_fundamental or reality_is_a_simulation)) → ethics_are_subjective)) then morality_is_arbitrary",
    "not ((existence_has_a_purpose and life_is_inherently_good) → (suffering_is_meaningful and (truth_is_absolute or morality_is_universal)))",
]

natural_restricted_sentences_debate_part_2 = [
    # Fundamental Philosophical Conundrums
    "if (existence_is_contingent and causality_is_universal) then (the_universe_has_a_cause or not nothing_can_exist)",
    "if (consciousness_requires_matter and matter_is_illusory) then (consciousness_is_an_illusion or reality_is_unfathomable)",
    "if (truth_is_relative and perception_defines_reality) then (knowledge_is_subjective or objectivity_is_inaccessible)",
    "if ((time_is_linear or time_is_cyclic) and (not time_is_discrete)) then (eternity_is_real or temporality_is_a_mental_construct)",
    "if (good_and_evil_are_subjective and morality_is_culturally_defined) then (justice_is_an_illusion or fairness_is_arbitrary)",
    
    # Cosmological and Metaphysical Paradoxes
    "if (the_universe_is_infinite and infinity_is_unintelligible) then (the_universe_is_incomprehensible or mathematics_is_flawed)",
    "if ((entropy_always_increases and the_universe_is_finite) or (entropy_is_reversible)) then (heat_death_is_inevitable or perpetual_motion_is_possible)",
    "if (existence_requires_observation and reality_is_independent) then (existence_is_dual or observation_defines_reality)",
    "if (if multiple_dimensions_exist then string_theory_is_correct) then (if string_theory_is_correct then dimensions_are_infinite)",
    "if (the_universe_is_a_simulation and the_simulator_is_unknowable) then (truth_is_a_lie or existence_is_an_experiment)",
    
    # Ethical Dilemmas and Moral Philosophy
    "if (if altruism_is_genetic then morality_is_evolved) then (ethics_are_biological or not moral_responsibility_exists)",
    "if (pain_is_unavoidable and happiness_is_fleeting) then (existence_is_suffering or hedonism_is_unjustifiable)",
    "if (justice_requires_power and power_is_corrupting) then (justice_is_corrupt or equality_is_unattainable)",
    "if ((freedom_requires_responsibility and morality_is_subjective) or (ethics_are_relative)) then (freedom_is_an_illusion or responsibility_is_absurd)",
    "if (environmental_destruction_is_inevitable and progress_is_necessary) then (sustainability_is_impossible or progress_is_a_mistake)",
    
    # Epistemological Quandaries
    "if (knowledge_is_experiential and experience_is_limited) then (knowledge_is_incomplete or certainty_is_impossible)",
    "if (if reality_is_a_hologram then perception_is_key) then (truth_is_illusory or knowledge_is_contextual)",
    "if (infinity_cannot_be_comprehended and the_universe_is_finite) then (human_cognition_is_inadequate or reality_is_non_finite)",
    "if (if logic_is_inconsistent then mathematics_is_invalid) then (reality_is_absurd or human_reasoning_is_fallible)",
    "if ((perception_shapes_reality and perception_is_flawed) or (truth_is_absolute)) then (reality_is_an_illusion or objectivity_is_incomplete)",
    
    # Sociological and Anthropological Perspectives
    "if (society_requires_hierarchy and equality_is_a_myth) then (freedom_is_unattainable or social_order_is_inevitable)",
    "if (language_shapes_thought and language_is_imperfect) then (thought_is_flawed or understanding_is_limited)",
    "if (cultural_progress_is_relative and history_is_written_by_victors) then (truth_is_political or knowledge_is_power)",
    "if ((individual_freedom_conflicts_with_social_cohesion and morality_is_contextual) or (justice_is_an_invention)) then (society_is_unsustainable or morality_is_futile)",
    "if (if nationalism_conflicts_with_globalism then cooperation_is_unsustainable) then (peace_is_impossible or progress_is_localized)",
    
    # Theological and Existential Challenges
    "if (god_is_all_knowing and free_will_exists) then (paradoxes_define_reality or omniscience_is_limited)",
    "if (if god_is_omnibenevolent then evil_is_an_illusion) then (suffering_is_purposeless or morality_is_finite)",
    "if (faith_requires_reason and reason_requires_doubt) then (faith_is_self_defeating or doubt_is_a_virtue)",
    "if (eternal_life_is_possible and death_gives_life_meaning) then (immortality_is_absurd or meaning_is_illusory)",
    "if ((heaven_requires_perfection and perfection_is_static) or (perfection_is_unattainable)) then (heaven_is_stagnant or progress_is_pointless)",
    
    # Technological and Post-Human Paradigms
    "if (ai_surpasses_human_intelligence and humans_control_ai) then (ai_is_benevolent or control_is_unsustainable)",
    "if (human_identity_is_data and data_is_replicable) then (selfhood_is_an_illusion or immortality_is_attainable)",
    "if (posthumanism_requires_transhumanism and transhumanism_requires_technology) then (humanity_is_obsolete or progress_is_unethical)",
    "if (technological_advancement_is_exponential and ethics_are_static) then (morality_cannot_keep_up or progress_is_dystopian)",
    "if ((virtual_reality_is_indistinguishable_from_reality and reality_is_subjective) or (truth_is_unverifiable)) then (existence_is_redundant or simulation_is_reality)",
]
