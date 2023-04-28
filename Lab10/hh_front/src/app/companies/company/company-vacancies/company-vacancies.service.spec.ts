import { TestBed } from '@angular/core/testing';

import { CompanyVacanciesService } from './company-vacancies.service';

describe('CompanyVacanciesService', () => {
  let service: CompanyVacanciesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CompanyVacanciesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
